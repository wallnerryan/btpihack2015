#!/usr/bin/env python

# Use python bluetooth bindings
import bluetooth

# List the currently seen devices
for device_address, name in bluetooth.discover_devices(flush_cache=True, lookup_names=True):
   print "Device: %s -> %s" % (device_address, name) 

