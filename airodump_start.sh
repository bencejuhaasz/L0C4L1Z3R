#!/bin/bash
rm tmp/*
echo "essid: "
read essid
echo "iface: "
read iface
airodump-ng --output-format csv -w ./tmp/csv --essid $essid $iface

