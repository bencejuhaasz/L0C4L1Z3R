#!/bin/bash

PS3='Please enter your choice: '
options=("WiFi" "RTL-SDR" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "WiFi")
            echo "essid: "
	    read essid
	    echo "interface: "
	    read interface
	    airodump-ng --output-format csv --essid $essid -w ./tmp/csv $interface > /dev/null 2>&1
	    python3 L0C_WiFi.py
            ;;
        "RTL-SDR")
            echo "you chose choice 2"
            ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done

