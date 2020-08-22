#!/bin/env python
# -*- coding: utf-8 -*- #
# Created And Coded by RC Chuah

# Import Modules
import os
import sys
import time
import datetime

os.system("clear")

# Information
print("Kali-Nethunter-In-Termux Installer v1.0")
print("")
print("Script By RC Chuah")
print("")
now = datetime.datetime.now()
print("Current date and time : ")
print(now.strftime("%d-%m-%Y %H:%M:%S"))
print("")
print("[1]-Install Kali Nethunter In Termux Full Version")
print("[2]-Install Kali Nethunter In Termux Minimal Version")
print("[3]-Uninstall Kali Nethunter In Termux")
print("[4]-Exit Installer")
print("")

# Main 
choice = input("Choice: ")
if choice == "1":
	os.system("apt update -y > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && cd ${HOME} && wget https://raw.githubusercontent.com/rc-chuah/Kali-Nethunter-In-Termux/master/install-nethunter-full-termux -q && chmod +x install-nethunter-full-termux && bash install-nethunter-full-termux && rm -rf kalifs-armhf-full.tar.xz && rm -rf kalifs-arm64-full.tar.xz && rm -rf kalifs-armhf-full.sha512sum && rm -rf kalifs-arm64-full.sha512sum && rm -rf ${HOME}/install-nethunter-full-termux")
if choice == "2":
	os.system("apt update -y > /dev/null 2>&1 && apt --assume-yes install wget > /dev/null 2>&1 && cd ${HOME} && wget https://raw.githubusercontent.com/rc-chuah/Kali-Nethunter-In-Termux/master/install-nethunter-minimal-termux -q && chmod +x install-nethunter-minimal-termux && bash install-nethunter-minimal-termux && rm -rf kalifs-armhf-minimal.tar.xz && rm -rf kalifs-arm64-minimal.tar.xz && rm -rf kalifs-armhf-minimal.sha512sum && rm -rf kalifs-arm64-minimal.sha512sum && rm -rf ${HOME}/install-nethunter-minimal-termux")
if choice == "3":
	os.system("rm -rf ${HOME}/kali-arm64 && rm -rf ${HOME}/kali-armhf && rm -rf ${PREFIX}/bin/nh && rm -rf ${PREFIX}/bin/nethunter && sleep 1 && echo Successfully Uninstalled !!!!!!")
if choice == "4":
	sys.exit()
elif choice == "":
    print("You Haven't Select Any Option From The Above !!!")
    print("Please Run This Script Again !!!")


