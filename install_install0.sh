# install divers software for testing

# python 3.
https://www.liquidweb.com/kb/how-to-install-and-update-python-to-3-9-in-ubuntu/

```
sudo apt update
sudo apt install python3.9 python3.9-venv python3.9-dev
python3.9 -V
```

```
sudo update-alternatives --install /usr/bin/python python /usr/bin/python2.7 1
sudo update-alternatives --install /usr/bin/python3.6.9 python /usr/bin/python3 2
sudo update-alternatives --install /usr/bin/python3 python /usr/bin/python3.9 3
sudo update-alternatives --config python
python3
   95  sudo update-alternatives --config python
   96  pip3 install virtualenv
   97  python3 -m virtualenv -p python3 env --system-site-packages
   98  . .bashrc


