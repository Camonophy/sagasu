#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Please run this setup file with root priviliges."
    exit 1
fi

pip uninstall binaryornot
python -m pip install git+https://github.com/Camonophy/binaryornot.git
sudo cp sagasu.py /bin/sagasu
sudo chmod 777 /bin/sagasu
