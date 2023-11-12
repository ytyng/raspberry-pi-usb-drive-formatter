#!/usr/bin/env python3

import time

import RPi.GPIO as GPIO


def main():
    GPIO.setwarnings(False)

    led_pin = 3
    GPIO.setmode(GPIO.BCM)
    GPIO.setup(led_pin, GPIO.OUT)

    for _ in range(3):
        GPIO.output(led_pin, True)
        time.sleep(0.5)
        GPIO.output(led_pin, False)
        time.sleep(0.5)


if __name__ == '__main__':
    main()
