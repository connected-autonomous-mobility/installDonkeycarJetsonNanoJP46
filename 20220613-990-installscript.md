# Installation using Ed Murphy's script

## 1. get install script 
- [x] get autorope/donkeycar, branch 990-jetson-nano-install-script

## 2. get python 3.7.13
- [x] install pyenv
- [x] pyenv install 3.7.13
- [x] add pyenv global 3.7.13 to install script

## 3. fix broken cv2
- [x] install opencv following https://automaticaddison.com/how-to-install-opencv-4-5-on-nvidia-jetson-nano/
- [x] pip install opencv-python

## 4. test lidar
```
sudo adduser $USER dialout
sudo chown :rainer /dev/ttyUSB0
sudo ls -l /dev/tty*
cd projects/donkeycar/donkeycar/parts/
python lidar.py 

```
