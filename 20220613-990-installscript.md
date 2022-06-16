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

Bus 001 Device 010: ID 10c4:ea60 Cygnal Integrated Products, Inc. CP210x UART Bridge / myAVR mySmartUSB light


```
## 5. fix CSI camera
- [ ] not solved yet
- [ ] https://github.com/mad4ms/python-opencv-gstreamer-examples/blob/master/gst_intel_device_to_app_to_file.py
- [x] sudo usermod -a -G video $LOGNAME
- [x] install: https://lifestyletransfer.com/how-to-launch-gstreamer-pipeline-in-python/
- [x] works: ~/projects/gst-python-tutorials$ python launch_pipeline/pipeline_with_parse_launch.py -p "nvarguscamerasrc sensor_id=0 ! nvoverlaysink"

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

## 6 autoconnect bluetooth joystick
- [x] install https://github.com/jrouleau/bluetooth-autoconnect
- [x] start every minute with crontab, ok quick & dirty but works
```
(env) rainer@jetsonautoware46:~/projects/CSI-Camera$ sudo crontab -l
# Edit this file to introduce tasks to be run by cron.
# 
# Each task to run has to be defined through a single line
# indicating with different fields when the task will be run
# and what command to run for the task
# 
# To define the time you can provide concrete values for
# minute (m), hour (h), day of month (dom), month (mon),
# and day of week (dow) or use '*' in these fields (for 'any').# 
# Notice that tasks will be started based on the cron's system
# daemon's notion of time and timezones.
# 
# Output of the crontab jobs (including errors) is sent through
# email to the user the crontab file belongs to (unless redirected).
# 
# For example, you can run a backup of all your user accounts
# at 5 a.m every week with:
# 0 5 * * 1 tar -zcf /var/backups/home.tgz /home/
# 
# For more information see the manual pages of crontab(5) and cron(8)
# 
# m h  dom mon dow   command
* * * * * sudo /usr/local/bin/bluetooth-autoconnect
```

## 7 fix servo
https://forums.developer.nvidia.com/t/jetpack-4-3-l4t-r32-3-1-released/109271/12
```
In my case, dtb files are under /boot/ , while script expects /boot/dtb/

the following change works for me.

line 135@/opt/nvidia/jetson-io/Jetson/board.py.

    #dtbdir = os.path.join(self.bootdir, 'dtb')
    dtbdir = os.path.join(self.bootdir, '')
```
```
Configuration saved to file                     |
 |     /boot/tegra210-p3448-0000-p3449-0000-a02-user-custom.dtb.      |
 |                                                                    |
 |     Press any key to reboot the system now or Ctrl-C to abort 
```

## udev
```
rainer@jetsonautoware46:~$ sudo cat /sys/kernel/debug/usb/devices | grep -E "^([TSPD]:.*|)$"
[sudo] password for rainer: 

T:  Bus=01 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=480  MxCh= 5
D:  Ver= 2.00 Cls=09(hub  ) Sub=00 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=1d6b ProdID=0002 Rev= 4.09
S:  Manufacturer=Linux 4.9.253-tegra xhci-hcd
S:  Product=xHCI Host Controller
S:  SerialNumber=70090000.xusb

T:  Bus=01 Lev=01 Prnt=01 Port=01 Cnt=01 Dev#=  2 Spd=480  MxCh= 4
D:  Ver= 2.10 Cls=09(hub  ) Sub=00 Prot=02 MxPS=64 #Cfgs=  1
P:  Vendor=0bda ProdID=5411 Rev= 1.20
S:  Manufacturer=Generic
S:  Product=4-Port USB 2.1 Hub

T:  Bus=01 Lev=02 Prnt=02 Port=00 Cnt=01 Dev#=  4 Spd=12   MxCh= 0
D:  Ver= 2.00 Cls=00(>ifc ) Sub=00 Prot=00 MxPS= 8 #Cfgs=  1
P:  Vendor=04fc ProdID=0801 Rev=16.11
S:  Manufacturer=MLK
S:  Product=USB Multi-Smart Mouse

T:  Bus=01 Lev=02 Prnt=02 Port=01 Cnt=02 Dev#=  5 Spd=12   MxCh= 0
D:  Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS= 8 #Cfgs=  1
P:  Vendor=258a ProdID=001f Rev= 6.27
S:  Manufacturer=SINO WEALTH
S:  Product=Mechanical Keyboard

T:  Bus=01 Lev=02 Prnt=02 Port=02 Cnt=03 Dev#=  6 Spd=12   MxCh= 0
D:  Ver= 1.10 Cls=00(>ifc ) Sub=00 Prot=00 MxPS=64 #Cfgs=  1
P:  Vendor=10c4 ProdID=ea60 Rev= 1.00
S:  Manufacturer=Silicon Labs
S:  Product=CP2102 USB to UART Bridge Controller
S:  SerialNumber=0001

T:  Bus=01 Lev=02 Prnt=02 Port=03 Cnt=04 Dev#=  7 Spd=480  MxCh= 0
D:  Ver= 2.00 Cls=ef(misc ) Sub=02 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=046d ProdID=0826 Rev= 0.10
S:  Product=HD Webcam C525
S:  SerialNumber=B03731F0

T:  Bus=01 Lev=01 Prnt=01 Port=02 Cnt=02 Dev#=  3 Spd=12   MxCh= 0
D:  Ver= 2.00 Cls=e0(wlcon) Sub=01 Prot=01 MxPS=64 #Cfgs=  1
P:  Vendor=8087 ProdID=0a2b Rev= 0.10

T:  Bus=02 Lev=00 Prnt=00 Port=00 Cnt=00 Dev#=  1 Spd=5000 MxCh= 4
D:  Ver= 3.00 Cls=09(hub  ) Sub=00 Prot=03 MxPS= 9 #Cfgs=  1
P:  Vendor=1d6b ProdID=0003 Rev= 4.09
S:  Manufacturer=Linux 4.9.253-tegra xhci-hcd
S:  Product=xHCI Host Controller
S:  SerialNumber=70090000.xusb

T:  Bus=02 Lev=01 Prnt=01 Port=00 Cnt=01 Dev#=  2 Spd=5000 MxCh= 4
D:  Ver= 3.20 Cls=09(hub  ) Sub=00 Prot=03 MxPS= 9 #Cfgs=  1
P:  Vendor=0bda ProdID=0411 Rev= 1.20
S:  Manufacturer=Generic
S:  Product=4-Port USB 3.1 Hub
```
