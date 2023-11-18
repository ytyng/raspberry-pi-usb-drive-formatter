#!/usr/bin/env bash

# This script use for debug.

echo "--------------------------------------------------------"
echo "usb-storage-formatter log.sh"
echo "$(date +%Y-%m-%d\ %H:%M:%S)"
echo "pwd: $(pwd)"
echo "whoami: $(whoami)"
echo "args: $*"
env

echo "--------------------------------------------------------"
echo "ls -l /dev/sd*"
ls -l /dev/sd*
