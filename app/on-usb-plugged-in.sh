#!/bin/bash

# This script is run when a USB device is plugged in.

LOG_FILE=/var/log/usb-storage-formatter/usb-storage-formatter.log

if [ ! -d "$LOG_DIR" ]; then
  mkdir -p "$LOG_DIR"
fi

if [ $$ -ne $(pgrep -fo "$0") ]; then
  echo "[$(date +%Y-%m-%d\ %H:%M:%S)] $$: $0 is already running. Exiting." >> ${LOG_FILE}
  exit 1
fi
# DEVNAME=/dev/sda
# DEVTYPE=disk
cd $(dirname $0)

./log.sh >> ${LOG_FILE} 2>&1

# ./format-usb-storage.sh >> ${LOG_FILE} 2>&1
