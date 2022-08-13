# Following Ed's installation script on a donkeycar

## 1 setup
1. hardware donkeycar: [Jetson Nano 4GB, CSI-camera, Adafruit PWM hat](https://github.com/connected-autonomous-mobility/50-hardware/blob/master/build_hardware_ValleyCrawler.md)
2. image: NVIDIA: jp46
3. software version 1: classical donkey with Ed's script, donkeycar 4.3.17?
4. software version 2: docker with naisy/donkeycar-jetson:overdrive4, jp46

## 2 error
command 
```donkey calibrate --channel 1/0 --bus 1``` 
works perfectly in both settings for both steering & throttle

command
```python manage.py drive``` 
the steering goes maximum right.

## 3 checked
- [x] steering & throttle in manage.py and pwm pulses in actuator.py. They are correct in both software versions.
- [x] with drivettrain setting *I2C* and the new *PWM_ ...*
- [x] Jetson Expansion Header Tool shows pwm0(32) and pwm2(33) as it should be
- [x] used the webcontroller

## 4 to be checked
- [ ] create own joystick to be sure angle & throttle are given correctly
- [ ] check debug output
- [ ] test driving with a plain pwm-joystick script that hardware is ok
- [ ] test with jp461 inkl. naisy docker

## 5 related
- https://github.com/autorope/donkeycar/issues/989

*Any ideas what else to check? Could that be some kind of hardware failure or a specialty of Jetson Nano gpio?*

## Solved
Hardware error!
