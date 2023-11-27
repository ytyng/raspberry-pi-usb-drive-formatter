#!/usr/bin/env python3
"""
Write this line to /etc/rc.local then sound will be played on boot:
BEEP_PIN=<BEEP_PIN_GPIO_NUMBER> /opt/usb-storage-formatter/power_on_beep.py
"""
import os
import time

import RPi.GPIO as GPIO


def main():
    beep_pin = os.environ.get('BEEP_PIN')
    if not beep_pin:
        print('no env BEEP_PIN', beep_pin)
        return 1
    beep_pin = int(beep_pin)
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(beep_pin, GPIO.OUT)
    pwm = GPIO.PWM(beep_pin, 1000)
    pwm.start(50)
    time.sleep(0.5)
    pwm.stop()


if __name__ == '__main__':
    exit(main())
