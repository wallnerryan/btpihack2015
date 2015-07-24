#!/usr/bin/env python

# Load data into an existing metadata container

"""
load_data -f /path/to/file.txt -o /container/path/ -c container-1
"""

import optparse
import os
import subprocess
import re
       
def main():
  p = optparse.OptionParser()
  p.add_option('--file', '-f', default="data.txt")
  p.add_option('--container', '-c', default="container")
  p.add_option('--cpath', '-o', default="/home/")
  p.add_option('--name', '-n', default="received_data")
  options, arguments = p.parse_args()
  print 'Loading %s' % options.file
  print 'Into %s' % options.container
  print 'At %s%s' % (options.cpath, options.name)

  
  os.system('docker exec %s bash -c "nc -l 4444 > %s%s" &' % (options.container, options.cpath, options.name))  
  proc = subprocess.Popen(["docker inspect %s | grep -i ipaddress" % options.container], stdout=subprocess.PIPE, shell=True)
  (out, err) = proc.communicate()
  ip = re.findall( r'[0-9]+(?:\.[0-9]+){3}', out )[0]
  os.system('netcat %s 4444 < %s' % (ip, options.file))
         
if __name__ == '__main__':
  main()
