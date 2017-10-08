import math
import time
import socket
from subprocess import call

k1 = []

def string2float(s):
    try:
        return(float(s))
    except:
        return(s)

def convert_deg2rad(deg):
    rad = (deg / 180) * math.pi
    return rad

def FlushSock():
    global sock
    sock.setblocking(False)
    while 1:
        try:
            PacketBytes = sock.recv(1024)
        except:
            break;
    sock.setblocking(True)

def convert_m2lat(m):
    global lat
    lat_K =  40075560 #6371001 * math.cos(lat)
    lat2 = m / (lat_K/360)
    return lat2

def convert_lat2m(lat):
    lat_K =  40075560
    m = lat * (lat_K/360)
    return(m)

def convert_m2lon(m):
    lon = m / (30000000/360)
    return(lon)

def convert_lon2m(lon):
    m = (30000000/360) * lon
    return(m)


#####################################

UDP_IP = "0.0.0.0"
UDP_PORT = 5005

sock = socket.socket(socket.AF_INET, # Internet
                     socket.SOCK_DGRAM) # UDP
sock.bind((UDP_IP, UDP_PORT))

###################################

i = 0
x1 = []
m1 = []
y1 = []
exit = False

min_pwr = input('minimum rxpower if the antenna is pointed at the signal source: ')

while(True):
    #call(["ls", "-l"])
    call(["rm", "./tmp/*"])
    call(["rtl_power", "-f", "88M:89M:20k", "./tmp/radio.csv", "-i", "1", "-e", "1"])
    f = open("./tmp/radio.csv")
    pwr = f.readline().split(",")[38].strip()
    print(pwr)
    pwr = float(pwr)
    min_pwr = float(min_pwr)
    FlushSock()
    while(not exit):
        try:
            data, addr = sock.recvfrom(1024)
            data = str(data)
            x = data.split(",")[28].strip()
            y = data.split(",")[29].strip()
            lat = data.split(",")[2].strip()
            lat = float(lat)
            lon = data.split(",")[3].strip()
            lon = float(lon)
            h = data.split(",")[4].strip()  
            print(x, y, lat, lon, h)
            exit = True
            break
        except(IndexError):
            pass
        
        
    data1, addr = sock.recvfrom(1024)
    data1 = str(data1)
    if(data1 != data and len(data1) == 247):
        data = data1
        x = data.split(",")[28].strip()
        y = data.split(",")[29].strip()
        lat = data.split(",")[2].strip()
        lat = float(lat)
        lon = data.split(",")[3].strip()
        lon = float(lon)
        h = data.split(",")[4].strip()
        if(len(data) != 67):
            hdg = convert_deg2rad(float(x))
            vert_deg = convert_deg2rad(float(y))                    
        print(x, y, lat, lon, h)            
        gps = 1
            
    if(data1 != data and len(data1) != 247):
        data = data1
        data = data.split(",")
        x = data[len(data)-3]
        y = data[len(data)-2]
        if(len(data) != 67):
            hdg = convert_deg2rad(float(x))
            vert_deg = convert_deg2rad(float(y))                
        gps = 0            
            
    if((gps == 1 and float(pwr) >= min_pwr) or i == 0):
        if(len(data) != 67):
            hdg = convert_deg2rad(float(x))
            vert_deg = convert_deg2rad(float(y))              
        r = 1
        a = float(h) * math.sin(vert_deg)
        Bdifflatm = a * math.sin(hdg)
        Bdifflonm = a * math.cos(hdg)
        difflat = convert_m2lat(Bdifflatm)
        difflon = convert_m2lon(Bdifflonm)
        B0lat = float(lat) + float(difflat)
        B0lon = float(lon) + float(difflon)        
    avglat = 0
    avglon = 0
    x1.append((B0lat - lat))
    y1.append((B0lon - lon))     
    if((lat - B0lat) != 0):
        m1.append((lon - B0lon) / (lat - B0lat))
    #print("#########")
    #print(str(len(y1))+" "+str(len(x1))+" "+str(len(m1))+" "+str(len(k1))+" "+str(i))
    #print("#########")
    k1.append(y1[i] - (x1[i] - m1[i]))
    
    if(i>=2 and (x1[i]*m1[i] + k1[i]) - (x1[i-1]*m1[i-1] + k1[i-1]) < r and float(pwr) >= min_pwr):
        avglon = convert_m2lon(y1[i]) + lon
        avglat = convert_m2lat(x1[i]) + lat
        a_ = (avglat - a)**2 + (avglon - a)**2
        b = 180 - 90 - vert_deg
        rh = a_ * math.tan(b)
        print("###############################")
        print("router_avg_pos: "+str(avglat)+" "+str(avglon)+" "+str(rh))
        print("###############################")               
         
    
    print("###############################")
    #print("Routerlat/Blon:")
    #print(str(B0lat)+" "+str(B0lon))
    #print("          ")
    print("lat/lon")
    print(str(lat)+" "+str(lon))
    print("         ")
    print("ALT:")
    print(str(h))
    print("           ")
    print("vert_deg:")
    print(str(vert_deg))
    print("hdg:")   
    print(str(x))
    print(str(hdg))
    print("src_ADDR:", addr)
    print("len_data:"+str(len(data)))
    #print("A: ", a)
    print("PWR: "+str(pwr))
    print("###############################")
    #print(data)
    i = i + 1
    time.sleep(1)
    gps = 0
    
