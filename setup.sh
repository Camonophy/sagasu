#!/bin/bash

if [[ $EUID -ne 0 ]]; then
    echo "Please run this setup file with root priviliges."
    exit 1
fi

DIR=$(pwd)

echo -e "#!/bin/bash \\n \\npython3 $DIR/sagasu.py \$@" >> sagasu
sudo chmod 777 sagasu 
mv sagasu /bin/
