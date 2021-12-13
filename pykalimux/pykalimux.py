#!/bin/env python
# -*- coding: utf-8 -*- #
# Created And Coded by RC Chuah-(RaynerSec)

# Import Modules
import os
import sys
import time
import datetime

# Press Enter To Continue Function
def press_enter():
    print("")
    input("Press Enter To Continue...")
    os.system("clear")

# Incorrect Selection Function
def incorrect_selection():
    print("Incorrect Selection! Try Again.")

# Main Function
def main():
  while True:
    # Usage Menu
    os.system("clear")
    print("Kali-Nethunter-In-Termux Installer")
    print("")
    print("Script By RC Chuah-(RaynerSec)")
    print("")
    now = datetime.datetime.now()
    print("Current Date And Time:")
    print(now.strftime("%d-%m-%y %H:%M:%S"))
    print("")
    print("[1]-Install Kali Nethunter In Termux Full Version")
    print("[2]-Install Kali Nethunter In Termux Minimal Version")
    print("[3]-Uninstall Kali Nethunter In Termux")
    print("[4]-Exit Menu")
    print("")
    choice = input("Enter Choice: ")
    # Menu Choices
    if choice == "1":
      os.system("clear")
      os.system("cd ${HOME} && curl -fsSL https://bit.do/fNyso | bash && rm -rf kalifs-armhf-full.tar.xz && rm -rf kalifs-arm64-full.tar.xz && rm -rf kalifs-armhf-full.sha512sum && rm -rf kalifs-arm64-full.sha512sum")
      press_enter()
    elif choice == "2":
      os.system("clear")
      os.system("cd ${HOME} && curl -fsSL https://bit.do/fNysW | bash && rm -rf kalifs-armhf-minimal.tar.xz && rm -rf kalifs-arm64-minimal.tar.xz && rm -rf kalifs-armhf-minimal.sha512sum && rm -rf kalifs-arm64-minimal.sha512sum")
      press_enter()
    elif choice == "3":
      os.system("clear")
      os.system("rm -rf ${HOME}/kali-arm64 && rm -rf ${HOME}/kali-armhf && rm -rf ${PREFIX}/bin/nh && rm -rf ${PREFIX}/bin/nethunter && sleep 1 && echo [+] Successfully Uninstalled ...")
      press_enter()
    elif choice == "4":
      os.system("clear")
      sys.exit()
    else:
      os.system("clear")
      incorrect_selection()
      press_enter()

# Driver Code
if __name__ == "__main__":
    main()
