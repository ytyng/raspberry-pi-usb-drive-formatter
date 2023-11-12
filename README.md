# raspberry-pi-usb-memory-formatter

Format usb memory when it is plugged in to Raspberry Pi.




## 参考
- [USB挿入でプログラムを実行する方法 - Raspberry Pi & Python 開発ブログ ☆彡](https://www.raspberrypirulo.net/entry/usb-script)
- [[linux]Raspberry PiでUSBメモリを刺すだけでフォーマットしてくれる装置を作る。 – Takeshi Igawa, Ph.D.](https://home.hiroshima-u.ac.jp/~tigawa/?p=2259)


## 参考情報

USB メモリを指した後の udevd から実行されるスクリプトの env
```
ID_FS_USAGE=filesystem
ID_PART_ENTRY_DISK=8:0
TAGS=:systemd:
ID_MODEL=Mass-Storage
ID_REVISION=1.11
ID_PART_ENTRY_NUMBER=1
ID_FS_LABEL_ENC=ESD-USB
ID_SERIAL=Generic_Mass-Storage-0:0
ID_PART_ENTRY_OFFSET=2048
ID_BUS=usb
ID_PATH=platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-scsi-0:0:0:0
ID_FS_TYPE=vfat
ID_FS_UUID=2822-C957
PWD=/
SEQNUM=2039
ID_MODEL_ID=0226
ID_VENDOR_ENC=Generic\x20
ID_PART_ENTRY_SIZE=15351808
DEVPATH=/devices/platform/scb/fd500000.pcie/pci0000:00/0000:00:00.0/0000:01:00.0/usb1/1-1/1-1.2/1-1.2:1.0/host0/target0:
0:0/0:0:0:0/block/sda/sda1
ID_PART_ENTRY_SCHEME=dos
USEC_INITIALIZED=69265891979
ID_VENDOR_ID=1908
ID_PART_ENTRY_UUID=d4e087b6-01
ID_FS_UUID_ENC=2822-C957
SUBSYSTEM=block
ID_INSTANCE=0:0
ID_USB_INTERFACES=:080650:
MINOR=1
ID_PART_ENTRY_TYPE=0xc
ID_PART_TABLE_UUID=d4e087b6
ID_MODEL_ENC=Mass-Storage\x20\x20\x20\x20
ID_FS_LABEL=ESD-USB
ID_PATH_TAG=platform-fd500000_pcie-pci-0000_01_00_0-usb-0_1_2_1_0-scsi-0_0_0_0
CURRENT_TAGS=:systemd:
ID_FS_VERSION=FAT32
SHLVL=1
ID_USB_INTERFACE_NUM=00
ID_PART_TABLE_TYPE=dos
DEVTYPE=partition
ID_USB_DRIVER=usb-storage
DEVLINKS=/dev/disk/by-path/platform-fd500000.pcie-pci-0000:01:00.0-usb-0:1.2:1.0-scsi-0:0:0:0-part1 /dev/disk/by-uuid/28
22-C957 /dev/disk/by-label/ESD-USB /dev/disk/by-partuuid/d4e087b6-01 /dev/disk/by-id/usb-Generic_Mass-Storage-0:0-part1
ID_VENDOR=Generic
ID_TYPE=disk
ID_PART_ENTRY_FLAGS=0x80
MAJOR=8
PARTN=1
DEVNAME=/dev/sda1
ACTION=add
_=/usr/bin/env
```
