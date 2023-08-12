# deb-live-image
deb-live-image is a set of scripts that streamline the use of the live-build and live-config tools for creating custom Debian-live images.
    
## Usage:
To start building the custom Debian live image, make sure that the `live.sh` script has execution permissions with the following command:

    chmod 777 ./live.sh

With this action, we can now use the `live.sh` script to create the Debian image:

    ./live.sh [OPTIONS] [FILE]

## Options
The script in question requires an option to perform a task, and depending on the case, you may need to specify a file. To view the options, use the `-h` | `--help` option, and use the `-m` | `--man` option to see a manual page. Example:
    
    ./live.sh --help

or

    ./live.sh --man

For creating the configuration files for the Debian live image, use the `-c` | `--config` option, which will invoke the script located at `./conf/config.py`

    ./live.sh --config
    
- Note: In the `config.py` file, you can easily modify each parameter of the lb config command as well as the chroot files and packages to install.

After running the previous command, use the `-b` | `--build` option to start the live image creation. Remember to specify the name of the directory where the previously created configuration files are located.

    ./live.sh --build project_name

This will run the lb build command in the project directory, install and create the Debian live image. This process may take a few minutes and will require an active internet connection throughout. The command's output will be saved in a file named output.txt for later review in case of errors.

## Chroot files

To modify or add files in the chroot environment, use the `./debian_src/` directory and refer to additional information in the `README.md` file in the `./debian_src/` directory.

## Considerations
This set of scripts makes use of the live-config and live-build tools developed by the Debian team, so you should have these tools installed on your system for proper functioning:
- live-build
- live-config
- live-boot

For more information, please refer to: https://live-team.pages.debian.net/live-manual/html/live-manual/index.en.html
- Note: It is recommended to have the latest version of each tool to ensure that there are no errors during the installation and configuration of the live image.

## Report bugs or give suggestions
To notify errors in the program or give suggestions for it, write your request in the following email: <universepenguin@protonmail.com>
