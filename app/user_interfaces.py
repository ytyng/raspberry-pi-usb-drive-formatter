#!/usr/bin/env python3
"""
User interface helper script.
LED blinker and beeper.
"""
import os
import threading
import time

import RPi.GPIO as GPIO


class LEDBlinker(threading.Thread):
    """
    Usage:
    led_blinker = LEDBlinker(led_pin=3)
    led_blinker.start()
    ...
    led_blinker.stop()
    """

    def __init__(self, *, led_pin=None):
        super().__init__()
        self.stop_event = threading.Event()
        if not led_pin:
            self.led_pin = None
            return
        self.led_pin = int(led_pin)

    def run(self):
        if not self.led_pin:
            return
        GPIO.setup(self.led_pin, GPIO.OUT)

        while not self.stop_event.is_set():
            GPIO.output(self.led_pin, True)
            time.sleep(0.5)
            GPIO.output(self.led_pin, False)
            time.sleep(0.5)

    def stop(self):
        self.stop_event.set()


class Beeper:
    """
    Usage:
    beeper = Beeper(beep_pin=4)
    beeper.play('info')
    beeper.play('success')
    beeper.play('failed')
    """

    scores = {
        'info': [
            (500, 0.03),
            (1000, 0.1),
        ],
        'success': [
            (1000, 0.05),
            (2000, 0.05),
        ]
        * 3,
        'failed': [
            (200, 0.1),
            (0, 0.1),
            (200, 0.4),
        ],
    }

    def __init__(self, *, beep_pin=None):
        if not beep_pin:
            self.beep_pin = None
            return
        self.beep_pin = int(beep_pin)
        GPIO.setup(self.beep_pin, GPIO.OUT)

    def play(self, score_name):
        if not self.beep_pin:
            return
        score = self.scores.get(score_name)
        pwm = GPIO.PWM(self.beep_pin, score[0][0])
        for frequency, duration in score:
            if frequency == 0:
                time.sleep(duration)
                continue
            pwm.ChangeFrequency(frequency)
            pwm.start(50)
            time.sleep(duration)
            pwm.stop()

    def play_async(self, note):
        t = threading.Thread(target=self.play, args=(note,))
        t.start()
        return t


def demo():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    led_pin = os.environ.get('LED_PIN')
    beep_pin = os.environ.get('BEEP_PIN')
    print(f'LED_PIN={led_pin}, BEEP_PIN={beep_pin}')

    led_blinker = LEDBlinker(led_pin=led_pin)
    led_blinker.start()
    beeper = Beeper(beep_pin=beep_pin)
    beeper.play_async('info')
    print('Beeping info.')
    time.sleep(2)
    beeper.play_async('success')
    print('Beeping success.')
    time.sleep(2)
    beeper.play_async('failed')
    print('Beeping failed.')
    time.sleep(2)
    led_blinker.stop()


if __name__ == '__main__':
    demo()
