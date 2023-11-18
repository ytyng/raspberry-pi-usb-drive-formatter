#!/usr/bin/env python3
import datetime
import os
import subprocess
import sys
import time

import RPi.GPIO as GPIO
from user_interfaces import Beeper, LEDBlinker


class FailedToUnmount(Exception):
    pass


def main():
    devname = os.environ.get('DEVNAME')
    if not devname:
        print('DEVNAME is not set', file=sys.stderr)
        return 1

    # DEVNAME=/dev/sda when DEVTYPE=disk.
    part_name = devname + '1'

    label = os.environ.get('ID_FS_LABEL')
    if not label:
        label = 'UD' + datetime.date.today().strftime('%Y%m%d')

    command = ['sudo', 'mkfs.fat', '-F', '32', devname, '-n', label]
    print('Command:', command)

    led_pin = os.environ.get('LED_PIN')
    beep_pin = os.environ.get('BEEP_PIN')
    if led_pin or beep_pin:
        GPIO.setwarnings(False)
        GPIO.setmode(GPIO.BCM)

    dry_run = os.environ.get('DRY_RUN') == '1'

    beeper = Beeper(beep_pin=beep_pin)
    led_blinker = LEDBlinker(led_pin=led_pin)

    beeper.play('info')
    led_blinker.start()

    try:
        if not dry_run:
            wait_and_unmount(part_name)

            # TODO: Delete all partitions ...?
            print('Formatting...')
            output = subprocess.check_output(
                ['sudo', 'mkfs.fat', '-F', '32', part_name, '-n', label]
            )
            print('Output:', output)
        else:
            print('Dry run. Not formatting.')
            time.sleep(2)

    except Exception:
        led_blinker.stop()
        beeper.play('failed')
        raise

    led_blinker.stop()
    beeper.play('success')


def wait_and_unmount(part_name):
    for _ in range(10):
        try:
            print('Unmounting...', flush=True)
            # umount: /dev/sda1: not mounted. Why?
            print(subprocess.check_output(['umount', part_name]))
            # print(subprocess.check_output(
            #     ['sudo', '-u', 'pi', 'umount', part_name]
            # ))
            return
        except subprocess.CalledProcessError:
            print('Failed to unmount. Retrying...', flush=True)
            time.sleep(1)
    raise FailedToUnmount('Failed to unmount.')


if __name__ == '__main__':
    exit(main())
