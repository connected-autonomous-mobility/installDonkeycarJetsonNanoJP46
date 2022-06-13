# Installation using Ed Murphy's script

## 1. get install script 
- [x] prepare script
```
git clone https://github.com/autorope/donkeycar.git
checkout 990-jetson-nano-install-script
```
## 2. get python 3.7.13
- [x] install pyenv
- [x] pyenv install 3.7.13
- [x] add pyenv global 3.7.13 to install script

## 3. fix broken cv2
- [x] install opencv following https://automaticaddison.com/how-to-install-opencv-4-5-on-nvidia-jetson-nano/
- [x] pip install opencv-python

## 4. test lidar
- [x] testing lidar.py
```
sudo adduser $USER dialout
sudo chown :rainer /dev/ttyUSB0
sudo ls -l /dev/tty*
cd projects/donkeycar/donkeycar/parts/
python lidar.py 
```
## 5. fix CSI camera
- [ ] not solved yet

error
```
python manage.py drive
________             ______                   _________              
___  __ \_______________  /___________  __    __  ____/_____ ________
__  / / /  __ \_  __ \_  //_/  _ \_  / / /    _  /    _  __ `/_  ___/
_  /_/ // /_/ /  / / /  ,<  /  __/  /_/ /     / /___  / /_/ /_  /    
/_____/ \____//_/ /_//_/|_| \___/_\__, /      \____/  \__,_/ /_/     
                                 /____/                              

using donkey v4.3.14 ...
INFO:donkeycar.config:loading config file: /home/rainer/d2/config.py
INFO:donkeycar.config:loading personal config over-rides from myconfig.py
INFO:__main__:PID: 13475
cfg.CAMERA_TYPE CSIC
INFO:__main__:cfg.CAMERA_TYPE CSIC
Traceback (most recent call last):
  File "manage.py", line 853, in <module>
    meta=args['--meta'])
  File "manage.py", line 152, in drive
    capture_width=cfg.IMAGE_W, capture_height=cfg.IMAGE_H, gstreamer_flip=cfg.CSIC_CAM_GSTREAMER_FLIP_PARM)
  File "/home/rainer/projects/donkeycar/donkeycar/parts/camera.py", line 221, in __init__
    self.init_camera()
  File "/home/rainer/projects/donkeycar/donkeycar/parts/camera.py", line 249, in init_camera
    raise RuntimeError("Unable to open CSICamera.")
RuntimeError: Unable to open CSICamera.

```
