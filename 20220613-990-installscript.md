# Installation using Ed Murphy's script

- [x] get autorope/donkeycar, branch 990-jetson-nano-install-script
- [x] install pyenv
- [x] pyenv install 3.7.13
- [x] add pyenv global 3.7.13 to install script
- [x] install opencv following https://automaticaddison.com/how-to-install-opencv-4-5-on-nvidia-jetson-nano/
- [x] pip install opencv-python


```
  290  pip install opencv-python
  292  source env/bin/activate
  294  cd d2
  295  python manage.py drive
  301  cd lidar/
  311  sudo adduser $USER dialout
  317  sudo chown :rainer /dev/ttyUSB0
  318  sudo ls -l /dev/tty*
  319  python display-lidar.py 
```
