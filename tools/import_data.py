#!/usr/bin/env python

"""
This takes an exportes TAR and imports to new docker image.

import_data.py -f /opt/my-exported.tar -c <container-name>
import_data.py -f /opt/my-exported.tar -c <container-name> -t myimported000
"""

import optparse
import os
       
def main():
  p = optparse.OptionParser()
  p.add_option('--file', '-f', default="/opt/exported.tar")
  p.add_option('--container', '-c', default="container")
  p.add_option('--tag', '-t', default="imported000")
  options, arguments = p.parse_args()
  print 'Importing %s to %s:%s' % (options.file, options.container, options.tag)

  os.system('cat %s | docker import - %s:%s' % (options.file, options.container, options.tag))

if __name__ == '__main__':
  main()
