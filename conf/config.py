#! /usr/bin/python3
#
#   Installer live-build Debian
#
#   Debian | Installer and configuration of the Debian Live image
#   GitHub: https://github.com/TheWatcherMultiversal/deb-live-image
#
#   License: GPLv3 (GNU/General Public License version 3.0)
#
# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Include modules:

import subprocess
import os
from colorama import Fore
from time import sleep

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Development environment configuration:

print(Fore.GREEN + "\r\nConfiguring debian with live-config...\r\n" + Fore.RESET)

lb_file           = input("Project directory name: ")#----> Project directory name
lb_src            = "sebian_src"#-------------------------> Config Files

# Desktop enviroment:
print("\r\nDesktop environments:\r\n")
print("(" + Fore.YELLOW + "1" + Fore.RESET + ") - KDE")
print("(" + Fore.YELLOW + "2" + Fore.RESET + ") - GNOME")
print("(" + Fore.YELLOW + "3" + Fore.RESET + ") - XFCE\r\n")

while True:

    n = input("Sebian enviroment: ")

    if n == "1":
        enviroment_sebian = "kde"
        break
    elif n == "2":
        enviroment_sebian = "gnome"
        break
    elif n == "3":
        enviroment_sebian = "xfce"
        break
    else:
        print(Fore.RED + "\r\nIncorrect value!!!\r\n" + Fore.RESET)
        sleep(1.5)

# Current path:
pwd = subprocess.run("cd ../ && pwd", shell=True, capture_output=True, text=True)#---> Current directory
pwd = output = pwd.stdout.strip()

os.system(f"mkdir ../{lb_file}")#---> File build

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Configuration of the "lb config" command:

# Parameters:
iso_aplication       = "Live Build"
iso_volume           = "debian_12"
iso_preparer         = "your_name"
iso_publisher        = "Debian"
binary_images        = "iso-hybrid"
archive_areas        = "main non-free-firmware"
mode                 = "debian"
updates              = "true"
distribution         = "bookworm"
architecture         = "amd64"
interactive          = "shell"
cache                = "true"
# mirror_bootstrap   = "http://deb.debian.org/debian/"
debian_installer     = "none"
debian_installer_gui = "true"
bootloaders          = "syslinux"
apt                  = "apt"
apt_recommends       = "true"
security             = "true"

# Command "lb config"
os.system(f'cd ../{lb_file} && lb config --binary-images {binary_images} --mode {mode} --distribution {distribution} --architecture {architecture} --archive-areas "{archive_areas}" --iso-application "{iso_aplication}" --iso-volume "{iso_volume}" --iso-preparer "{iso_preparer}" --iso-publisher "{iso_publisher}" --bootloaders {bootloaders} --cache {cache} --updates {updates} --interactive {interactive} --linux-flavours {architecture}  --debian-installer {debian_installer} --debian-installer-gui {debian_installer_gui} --apt {apt} --apt-recommends {apt_recommends} --security {security}')

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Packages to add in packages-list:

if enviroment_sebian == "kde":
    Packages = ["grub2-common", "calamares", "calamares-settings-debian", "wget", "apt-transport-https", "flatpak", "plasma-discover-backend-flatpak", "latte-dock", "keepassxc", "network-manager", "lynis", "clamav", "clamtk", "rkhunter", "ufw", "wireshark", "tcpdump", "mc", "htop", "neofetch", "vlc", "elisa", "inkscape"]

elif enviroment_sebian == "gnome":
    Packages = ["grub2-common", "calamares", "calamares-settings-debian", "wget", "apt-transport-https", "flatpak", "keepassxc", "network-manager", "lynis", "clamav", "clamtk", "rkhunter", "ufw", "wireshark", "tcpdump", "mc", "htop", "neofetch", "vlc", "elisa" , "inkscape"]

elif enviroment_sebian == "xfce":
    Packages = ["grub2-common", "calamares", "calamares-settings-debian", "wget", "apt-transport-https", "flatpak", "keepassxc", "network-manager", "lynis", "clamav", "clamtk", "rkhunter", "ufw", "wireshark", "tcpdump", "mc", "htop", "neofetch", "vlc", "elisa" , "inkscape"]

# Environment:
enviroment = f"task-{enviroment_sebian}-desktop"

for i in Packages:
    os.system(f"cd ../{lb_file} && echo '{i}' >> ./config/package-lists/packages.list.chroot")

os.system(f"cd ../{lb_file} && echo '{enviroment}' > ./config/package-lists/desktop.list.chroot")

# ------------------------------------------------------------------ (*)
#   |
#   |
#   °-- Chroot configuration:

print(Fore.YELLOW + "\r\nCopying chroot files..." + Fore.RESET)

os.system(f"cp -r {pwd}/{lb_src}/debian_{enviroment_sebian}_chroot/etc {pwd}/{lb_file}/config/includes.chroot_before_packages/")

os.system(f"cp -r {pwd}/{lb_src}/debian_{enviroment_sebian}_chroot/usr {pwd}/{lb_file}/config/includes.chroot_before_packages/")

# Finish
print(Fore.GREEN + "\r\nProcess completed" + Fore.RESET + f", the image configuration is located at {pwd}/{lb_file}")