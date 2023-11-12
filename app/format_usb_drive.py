#!/usr/bin/env python3
import os
import sys

import subprocess
import datetime


def main():
    devname = os.environ.get('DEVNAME')
    if not devname:
        print('DEVNAME is not set', file=sys.stderr)
        return 1

    label = os.environ.get('ID_FS_LABEL')
    if not label:
        label = 'USBDRIVE_' + datetime.date.today().strftime('%Y%m%d')

    subprocess.check_output(
        ['sudo', 'mkfs.fat', '-F', '32', devname, '-n', label]
    )


if __name__ == '__main__':
    exit(main())
