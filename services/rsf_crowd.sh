#!/bin/bash
export $PATH="/usr/bin/python3"
source ~/.bashrc
source ~/.profile
echo "path = $PATH"
cd /home/ubuntu/RSF_Capacity_Alert
python3 discord_alert.py
