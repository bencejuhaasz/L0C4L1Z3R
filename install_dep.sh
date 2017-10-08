#!/bin/bash
apt install python3
PS3='Please enter your choice: '
options=("WiFi" "RTL-SDR" "Quit")
select opt in "${options[@]}"
do
    case $opt in
        "WiFi")
            apt install aircrack-ng
            ;;
        "RTL-SDR")
            apt install rtl-sdr
            ;;
        "Quit")
            break
            ;;
        *) echo invalid option;;
    esac
done
