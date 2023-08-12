#!/bin/bash

# live: startup script
# License: GNU General Public License v3.0
# Developed by: Angel Gabriel Mortera Gual
# Github project: https://github.com/TheWatcherMultiversal/deb-live-image

# Options

set -e

case "$1" in
-h|--help)

    echo $"
Usage: live [OPTIONS] [FILE]
      --help              print this help and exit
  -c, --config            creating configuration files with lb config
  -b, --build             image building process
  -m, --man               man page
"
        ;;
-c|--config)
        cd ./conf/ && python3 config.py
        exit 0
        ;;
-b|--build)
        echo "The following command requires superuser permissions, you can check the command's output in output.txt"
        cd ./$2 && sudo lb build 2>&1 | tee -a ../output.txt
        ;;  
-m|--man)
        man ./man/deb-live-image.1
        ;;
*)
        echo "specify an option, use live -m for more information"
        exit 1
esac