#!/usr/bin/env python3

import threading
import time

import RPi.GPIO as GPIO


class LEDBlinker(threading.Thread):
    def __init__(self, *, led_pin=3):
        super().__init__()
        self.led_pin = led_pin
        self.stop_event = threading.Event()

    def run(self):
        GPIO.setup(self.led_pin, GPIO.OUT)

        while not self.stop_event.is_set():
            GPIO.output(self.led_pin, True)
            time.sleep(0.5)
            GPIO.output(self.led_pin, False)
            time.sleep(0.5)

    def stop(self):
        self.stop_event.set()


def main():
    GPIO.setwarnings(False)

    GPIO.setmode(GPIO.BCM)

    led = LEDBlinker(led_pin=3)
    led.start()
    for _ in range(4):
        print('LED Blinking...', flush=True)
        time.sleep(0.7)
    led.stop()
    led.join()


if __name__ == '__main__':
    main()
