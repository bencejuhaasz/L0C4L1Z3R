# L0C4L1Z3R Dokumentáció

A program célja egy minden irányba egyenletesen sugárzó jelforrás
helyének meghatározása GPS, giroszkóp és irányított antenna segítségével.

## Rendszerkövetelmények:
- GNU/Linux (a dep_install.sh Debian alapú rendszereken működik)
- python3
- aircrack-ng programcsomag
- rtl-sdr driver
- a GPS/giroszkóp adatokat streamelő eszközön android
- hálózati kapcsolat a streamelő és az adatokat feldolgozó gép között (a két gép lehet ugyanaz)

## Hardverkövetelmények:
- az androidot futtató eszközben giroszkóp/GPS vevő
- wifi interface irányított antennával/ RTL-SDR rádióvevő irányított antennával csatlakoztatva a feldolgozó géphez
- a giroszkóp/GPS adatokat streamelő eszköznek együtt kell mozognia az antennával

