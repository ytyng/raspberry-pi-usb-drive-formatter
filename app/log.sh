#!/usr/bin/env bash

#

log_dir="/var/log/usb-memory-formatter"

if [ ! -d "$log_dir" ]; then
  sudo mkdir -p "$log_dir"
  sudo chown -R "$USER" "$log_dir"
fi

log_file="$log_dir/$(date +%Y%m%d).log"

echo "$(date +%Y-%m-%d\ %H:%M:%S) $*" >> "$log_file"
env >> "$log_file"
