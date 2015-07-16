
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

You should see your device name and devices mac address show up. You can use the other scripts called hcitool_devices.sh and nearby_devices.py which are vairations of this. 

```tools/list_services.py``` shows the services available from a bluetooth device.

You can expect output like the below
```
pi@raspberrypi ~/pi-hack-project $ python tools/find_services.py 
found 9 services on C8:1E:E7:7C:7F:41
()
Service Name: MAP MAS-iOS
    Host:        C8:1E:E7:7C:7F:41
    Description: None
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 2
    svc classes: ['1132'] 
    profiles:    [('1134', 256)] 
    service id:  None 
()
Service Name: PAN Network Access Profile
    Host:        C8:1E:E7:7C:7F:41
    Description: Network Access Point
    Provided By: None
    Protocol:    L2CAP
    channel/PSM: 15
    svc classes: ['1116'] 
    profiles:    [('1116', 256)] 
    service id:  None 
()
Service Name: Wireless iAP
    Host:        C8:1E:E7:7C:7F:41
    Description: None
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 1
    svc classes: ['00000000-DECA-FADE-DECA-DEAFDECACAFE'] 
    profiles:    [('1101', 256)] 
    service id:  None 
()
Service Name: AVRCP Device
    Host:        C8:1E:E7:7C:7F:41
    Description: Remote Control Device
    Provided By: None
    Protocol:    L2CAP
    channel/PSM: 23
    svc classes: ['110E', '110F'] 
    profiles:    [('110E', 260)] 
    service id:  None 
()
Service Name: AVRCP Device
    Host:        C8:1E:E7:7C:7F:41
    Description: Remote Control Device
    Provided By: None
    Protocol:    L2CAP
    channel/PSM: 23
    svc classes: ['110C'] 
    profiles:    [('110E', 260)] 
    service id:  None 
()
Service Name: Audio Source
    Host:        C8:1E:E7:7C:7F:41
    Description: None
    Provided By: None
    Protocol:    L2CAP
    channel/PSM: 25
    svc classes: ['110A'] 
    profiles:    [('110D', 259)] 
    service id:  None 
()
Service Name: Phonebook
    Host:        C8:1E:E7:7C:7F:41
    Description: None
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 13
    svc classes: ['112F'] 
    profiles:    [('1130', 256)] 
    service id:  None 
()
Service Name: Handsfree Gateway
    Host:        C8:1E:E7:7C:7F:41
    Description: None
    Provided By: None
    Protocol:    RFCOMM
    channel/PSM: 8
    svc classes: ['111F', '1203'] 
    profiles:    [('111E', 262)] 
    service id:  None 
()
Service Name: None
    Host:        C8:1E:E7:7C:7F:41
    Description: PnP Information
    Provided By: None
    Protocol:    None
    channel/PSM: None
    svc classes: ['1200'] 
    profiles:    [] 
    service id:  None 
()

```

If you wanted to pair using bluez tools run the ```utils/setkeyboarddisp.sh``` script so that pairing pops up a window on your phone. Then run the following

```
sudo bluez-simple-agent hci0 <MACADDRESS>

sudo bluez-test-device trusted <MACADDRESS> yes
```
