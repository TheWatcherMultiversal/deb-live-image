# Chroot files | debian_src
In this directory, you can host all the files you want to modify and add to the chroot environment of the Debian live image. To do this, you should create a directory with the following nomenclature so that the config.py file can find the desired path:
   
    mkdir debian_[ENVIROMENT]_chroot

Where you should replace `[ENVIROMENT]` with the chosen desktop environment, either kde, gnome, or xfce, and you should write it in lowercase to avoid errors.
- Note: This can be modified in the `config.py` file to assign other names to the chroot environment according to your preference.

Once the directory is created, we can add all the necessary files for configuring our chroot environment. You can refer to the `Filesystem Hierarchy Standard` (FHS) to organize the files properly.

For more information, refer to: https://access.redhat.com/documentation/en-us/red_hat_enterprise_linux/4/html/reference_guide/s1-filesystem-fhs
