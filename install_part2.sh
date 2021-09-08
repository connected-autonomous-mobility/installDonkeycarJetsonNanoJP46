# PART 2
# # script --timing install_dc_jp46_p2.log 

sudo usermod -aG dialout $USER
sudo systemctl disable nvgetty

# Step 5
pip3 install -U pip testresources setuptools
pip3 install -U futures==3.1.1 protobuf==3.12.2 pybind11==2.5.0
pip3 install -U cython==0.29.21 pyserial
pip3 install -U future==0.18.2 mock==4.0.2 h5py==2.10.0 keras_preprocessing==1.1.2    keras_applications==1.0.8 gast==0.3.3
pip3 install -U absl-py==0.9.0 py-cpuinfo==7.0.0 psutil==5.7.2 portpicker==1.3.1 six    requests==2.24.0 astor==0.8.1 termcolor==1.1.0 wrapt==1.12.1 google-pasta==0.2.0
pip3 install -U gdown

#pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v46 tensorflow
pip3 install --pre --extra-index-url https://developer.download.nvidia.com/compute/redist/jp/v45 tensorflow==2.3.1

wget https://nvidia.box.com/shared/static/p57jwntv436lfrd78inwl7iml6p13fzh.whl
cp p57jwntv436lfrd78inwl7iml6p13fzh.whl torch-1.8.0-cp36-cp36m-linux_aarch64.whl
pip3 install torch-1.8.0-cp36-cp36m-linux_aarch64.whl
sudo apt-get install libjpeg-dev zlib1g-dev libpython3-dev libavcodec-dev libavformat-dev libswscale-dev
mkdir -p ~/projects; cd ~/projects
git clone -b v0.9.0 https://github.com/pytorch/vision torchvision
cd ~/project/torchvision 
python setup.py install
cd ../

#pip3 install pyfiglet prettytable kivy plotly imgaug packaging docopt
#pip3 uninstall -y opencv-python #  fix thx to @naisy, Jetson has already installed OpenCV and generic does not work on Jetson

# Step 6
cd ~/projects
git clone https://github.com/autorope/donkeycar
cd donkeycar
git checkout dev
#git checkout master
pip3 install -e .[nano]

# Step 7 
wget https://www.dropbox.com/s/u80hr1o8n9hqeaj/camera_overrides.isp
sudo cp camera_overrides.isp /var/nvidia/nvcam/settings/
sudo chmod 664 /var/nvidia/nvcam/settings/camera_overrides.isp
sudo chown root:root /var/nvidia/nvcam/settings/camera_overrides.isp

# Step 8 
sudo apt-get install -y python-dev libsdl1.2-dev libsdl-image1.2-dev libsdl-mixer1.2-dev libsdl-ttf2.0-dev libsdl1.2-dev libsmpeg-dev python-numpy subversion libportmidi-dev ffmpeg libswscale-dev libavformat-dev libavcodec-dev libfreetype6-dev
pip3 install pygame

# lidar stuff
pip3 install glob2
pip3 install Adafruit_CircuitPython_RPLIDAR

# cleaning up
sudo apt autoremove -y

# install openCV
# https://qengineering.eu/install-opencv-4.5-on-jetson-nano.html

# install tensorflow
# https://qengineering.eu/install-tensorflow-2.4.0-on-jetson-nano.html

# end logging
#exit

