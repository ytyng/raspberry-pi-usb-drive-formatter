#!/bin/bash

# This script is run when a USB device is plugged in.

LOG_FILE=/var/log/usb-storage-formatter/usb-storage-formatter.log
LOG_DIR=$(dirname $LOG_FILE)

if [ ! -d "${LOG_DIR}" ]; then
  mkdir -p "${LOG_DIR}"
fi

# echo "DEVTYPE=${DEVTYPE}, ID_USB_DRIVER=${ID_USB_DRIVER}" >> ${LOG_FILE}

if [[ "${DEVTYPE}" != "disk" ]]; then
  echo "[$(date +%Y-%m-%d\ %H:%M:%S)] DEVTYPE (${DEVTYPE}) is not disk. Skipping." >> ${LOG_FILE}
  exit 0
fi

if [[ "${ID_USB_DRIVER}" != "usb-storage" ]]; then
  echo "[$(date +%Y-%m-%d\ %H:%M:%S)] ID_USB_DRIVER (${ID_USB_DRIVER}) is not usb-storage. Skipping." >> ${LOG_FILE}
  exit 0
fi

if [ $$ -ne $(pgrep -fo "$0") ]; then
  echo "[$(date +%Y-%m-%d\ %H:%M:%S)] $$: $0 is already running. Exiting." >> ${LOG_FILE}
  exit 1
fi

cd $(dirname $0)

# Load dotenv
set -a
source .env
set +a

# log for debug.
./log.sh >> ${LOG_FILE} 2>&1

./format_usb_storage.py >> ${LOG_FILE} 2>&1
