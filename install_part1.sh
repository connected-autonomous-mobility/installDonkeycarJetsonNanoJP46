# begin logging
#script --timing install_dc_jp46_p1.log # thx to @naisy!

# Step 3
sudo apt-get update -y
sudo apt-get upgrade -y
sudo apt-get install -y libhdf5-serial-dev hdf5-tools libhdf5-dev zlib1g-dev zip    libjpeg8-dev liblapack-dev libblas-dev gfortran
sudo apt-get install -y python3-dev python3-pip
sudo apt-get install -y libxslt1-dev libxml2-dev libffi-dev libcurl4-openssl-dev    libssl-dev libpng-dev libopenblas-dev
sudo apt-get install -y git nano
sudo apt-get install -y openmpi-doc openmpi-bin libopenmpi-dev libopenblas-dev

# Step 3.1 own utilities

# terminator
sudo add-apt-repository -y ppa:gnome-terminator
sudo apt-get update -y
sudo apt-get install -y terminator

# docker stuff
sudo apt-get install -y docker-compose 
sudo groupadd docker
sudo usermod -aG docker $USER
docker run hello-world

# camera stuff
sudo apt-get install -y v4l-utils
sudo apt-get install -y libcanberra-gtk-module libcanberra-gtk3-module
cd ~/dev; git clone https://github.com/JetsonHacksNano/CSI-Camera.git

# VScode
mkdir -p ~/dev;cd dev
git clone https://github.com/JetsonHacksNano/installVSCode.git
cd installVSCode
./installVSCodeWithPython.sh

# ROS2 local
cd ~/dev; git clone https://github.com/jetsonhacks/installROS2.git
# ./installROS2

# jetsonstats
sudo -H pip3 install -U jetson-stats
sudo systemctl restart jetson_stats.service

# increase swap space to 4GB
cd ~/dev; git clone https://github.com/JetsonHacksNano/resizeSwapMemory.git
cd resizeSwapMemory
./setSwapMemorySize.sh -g 4

# Step 4
cd ~
pip3 install virtualenv
python3 -m virtualenv -p python3 env --system-site-packages
echo "source env/bin/activate" >> ~/.bashrc
source ~/.bashrc

# end part 1
# REBOOT!
#
