
Pi Hack 2015
===========

### Dependencies

##### Libraries
- bluez-tools
- libbluetooth-dev
- blueman
- python
- python-dev
- git

##### Python Libs
PyBluez

##### Tools
Pi2 Bluetooth Dongle

### Purpose

The purpose of this repository is to supply documentation and code on how to prototype matadata movement with linux containers and bluetooth as a substrate for IoT purposes.

### How to use

Turn your iphone or other bluetooth device on and in discoverable state

```
root@raspberrypi:/home/pi/btrepo# python tools/list_devices.py 
Device: C8:1E:E7:7C:7F:41 -> Wally's iPhone
```

You should see your device name and devices mac address show up.
