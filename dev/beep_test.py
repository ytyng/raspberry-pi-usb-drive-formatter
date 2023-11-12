#!/usr/bin/env python3

import time

import RPi.GPIO as GPIO

beep_pin = 4

info_notes = [
    (500, 0.03),
    (1000, 0.1),
]

success_notes = [
    (1000, 0.05),
    (2000, 0.05),
] * 3

failed_notes = [
    (200, 0.1),
    (0, 0.1),
    (200, 0.4),
]


def play_beep(notes):
    pwm = GPIO.PWM(beep_pin, notes[0][0])
    for frequency, duration in notes:
        if frequency == 0:
            time.sleep(duration)
            continue
        pwm.ChangeFrequency(frequency)
        pwm.start(50)
        time.sleep(duration)
        pwm.stop()


def main():
    GPIO.setwarnings(False)
    GPIO.setmode(GPIO.BCM)

    GPIO.setup(beep_pin, GPIO.OUT)

    play_beep(info_notes)
    time.sleep(1)
    play_beep(success_notes)
    time.sleep(1)
    play_beep(failed_notes)


if __name__ == '__main__':
    main()
