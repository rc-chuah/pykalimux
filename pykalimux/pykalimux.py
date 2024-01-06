#!/bin/env python
# -*- coding: utf-8 -*- #
# Created And Coded by RC Chuah-(RaynerSec)

# Import Modules
import os
import sys
import time
import datetime

# Install Kali Nethunter In Termux Full Version Function
def full():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-full-termux | bash && rm -rf kalifs-armhf-full.tar.xz && rm -rf kalifs-arm64-full.tar.xz && rm -rf kalifs-armhf-full.sha512sum && rm -rf kalifs-arm64-full.sha512sum")

# Install Kali Nethunter In Termux Minimal Version Function
def minimal():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-minimal-termux | bash && rm -rf kalifs-armhf-minimal.tar.xz && rm -rf kalifs-arm64-minimal.tar.xz && rm -rf kalifs-armhf-minimal.sha512sum && rm -rf kalifs-arm64-minimal.sha512sum")

# Install Kali Nethunter In Termux Nano Version Function
def nano():
    os.system("cd ${HOME} && curl -fsSL https://bit.ly/install-nethunter-nano-termux | bash && rm -rf kalifs-armhf-nano.tar.xz && rm -rf kalifs-arm64-nano.tar.xz && rm -rf kalifs-armhf-nano.sha512sum && rm -rf kalifs-arm64-nano.sha512sum")

# Uninstall Kali Nethunter In Termux Function
def uninstall():
    os.system("rm -rf ${HOME}/kali-arm64 && rm -rf ${HOME}/kali-armhf && rm -rf ${PREFIX}/bin/nh && rm -rf ${PREFIX}/bin/nethunter && sleep 1 && echo [+] Successfully Uninstalled ...")

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
    print("[3]-Install Kali Nethunter In Termux Nano Version")
    print("[4]-Uninstall Kali Nethunter In Termux")
    print("[5]-Exit Menu")
    print("")
    choice = input("Enter Choice: ")
    # Menu Choices
    if choice == "1":
      os.system("clear")
      full()
      press_enter()
    elif choice == "2":
      os.system("clear")
      minimal()
      press_enter()
    elif choice == "3":
      os.system("clear")
      nano()
      press_enter()
    elif choice == "4":
      os.system("clear")
      uninstall()
      press_enter()
    elif choice == "5":
      os.system("clear")
      sys.exit()
    else:
      os.system("clear")
      incorrect_selection()
      press_enter()

# Driver Code
if __name__ == "__main__":
    main()
