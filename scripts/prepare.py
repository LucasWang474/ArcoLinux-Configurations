# Author: Lucas Wang
# Created: 2021-12-21
# Last Modified: 2021-12-21
# Description: Restore my ArcoLinux packages and configs after a fresh install.


import os
import shutil
import subprocess
import sys


# First check if the script is run as root.
print("\n\n\nChecking if script is run as root...")
if os.geteuid() != 0:
    print("Please run this script as root.")
    sys.exit(1)
else:
    print("Script is run as root.")


# Re-generate ArchLinux mirrorlist based on the country code.
print("\n\n\nRegenerating ArchLinux mirrorlist...")
subprocess.run(
    [
        "pacman",
        "--noconfirm",
        "--noprogressbar",
        "--config",
        "/etc/pacman.conf",
        "-Sy",
        "reflector",
    ]
)
subprocess.run(
    [
        "reflector",
        "--verbose",
        "--sort",
        "rate",
        "--country",
        "CN",
        "--save",
        "/etc/pacman.d/mirrorlist",
    ]
)
print("Regenerating ArchLinux mirrorlist done.")


# Edit `/etc/pacman.conf` to add `[archlinuxcn]` section.
# For more archlinuxcn repo info, see: https://github.com/archlinuxcn/mirrorlist-repo
print("\n\n\nEditing `/etc/pacman.conf` to add `[archlinuxcn]` section...")
with open("/etc/pacman.conf", "a") as f:
    if "[archlinuxcn]" not in open("/etc/pacman.conf").read():
        # Append `[archlinuxcn]` section.
        f.write("\n\n[archlinuxcn]\n")
        f.write("#Server = https://mirrors.sjtug.sjtu.edu.cn/archlinux-cn/$arch\n")
        f.write("#Server = https://mirrors.aliyun.com/archlinuxcn/$arch\n")
        f.write("#Server = https://mirrors.dgut.edu.cn/archlinuxcn/$arch\n")
        f.write("Server = https://mirrors.sustech.edu.cn/archlinuxcn/$arch\n")

        print("Added `[archlinuxcn]` section to `/etc/pacman.conf`.")
    else:
        print("`/etc/pacman.conf` already has `[archlinuxcn]` section.")


# Refresh the pacman cache and install keyrings.
print("\n\n\nRefreshing pacman cache and installing keyrings...")
subprocess.run(["pacman", "-Syy", "--noconfirm", "archlinux-keyring"])
subprocess.run(["pacman", "-Syy", "--noconfirm", "arcolinux-keyring"])
subprocess.run(["pacman", "-Syy", "--noconfirm", "archlinuxcn-keyring"])
print("Refreshing pacman cache and installing keyrings done.")


# Update the system.
print("\n\n\nUpdating system...")
subprocess.run(["pacman", "-Syyu", "--noconfirm"])
print("Updating system done.")
