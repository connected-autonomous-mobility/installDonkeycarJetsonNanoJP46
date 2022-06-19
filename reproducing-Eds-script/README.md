# Following Ed' installation script on a donkeycar


mysterious bug:
1. running on donkeycar with jetson nano, jp46
2. software version 1: classical donkey with Ed's script
3. software version 2: docker with naisy/donkeycar-jetson:overdrive4
4. doing ```donkey calibrate --channel 1/0 --bus 1``` works perfectly in both settings for both steering & throttle
But as soon as I start ```python manage.py drive``` the steering goes maximum right.

Already checked
- [x] steering & throttle in manage.py and pwm pulses in actuator.py. They are correct in both software versions.
- [x] with drivettrain setting *I2C* and the new *PWM_ ...*
- [x] Jetson Expansion Header Tool shows pwm0(32) and pwm2(33) as it should be
- [x] used the webcontroller

To be checked
- [ ] create own joystick to be sure angle & throttle are given correctly
- [ ] check debug output
- [ ] test driving with a plain pwm-joystick script that hardware is ok
- [ ] test with jp461 inkl. naisy docker

*Any ideas what else to check? Could that be some kind of hardware failure or a specialty of Jetson Nano gpio?*
