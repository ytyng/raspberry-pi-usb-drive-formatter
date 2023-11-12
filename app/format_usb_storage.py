#!/usr/bin/env python3
import os
import sys

import subprocess
import datetime

DRY_RUN = True


def main():
    devname = os.environ.get('DEVNAME')
    if not devname:
        print('DEVNAME is not set', file=sys.stderr)
        return 1

    label = os.environ.get('ID_FS_LABEL')
    if not label:
        label = 'USBDRIVE_' + datetime.date.today().strftime('%Y%m%d')

    command = ['sudo', 'mkfs.fat', '-F', '32', devname, '-n', label]
    print('Command:', command)

    if not DRY_RUN:
        print('Formatting...')
        output = subprocess.check_output(
            ['sudo', 'mkfs.fat', '-F', '32', devname, '-n', label]
        )
        print('Output:', output)


if __name__ == '__main__':
    exit(main())
