# diyrobocars_install_jp46
Automates (partly) the installation described at [donkeycar.com](https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/) for a Jetson Nano JP 4.6.

## Prerequisites

Prepare an SD-card with the latest Nvidia JetPack version (JP 4.6) for Jetson Nano following [donkeycar.com](https://docs.donkeycar.com/guide/robot_sbc/setup_jetson_nano/), do your first time boot and clone the repo.
```
git clone https://github.com/connected-autonomous-mobility/diyrobocars_install_jp46.git
cd diyrobocars_install_jp46
```

## 1 Preparation

Log the installation for debugging purposes. (thx to @Naisy for this great tip :-)
```
script install_dc_jp46_p1.log
```

Start part 1
```
./install_dc_jp4_v2p1.sh
```
hint: part 1 requires one input from you right near the beginning to confirm restart of the docker aservice after uptdating.

## 2 Reboot
```
sudo reboot
```

## 3 Installation
Log the installation for debugging purposes.
```
script install_dc_jp46_p2.log
```
```
./install_dc_jp4_v2p2.sh
```
Terminate logging
```
exit
````
