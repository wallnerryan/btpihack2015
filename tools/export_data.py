#!/usr/bin/env python

# This exports the metadata container and saves it to a .tar file.
# The TAR file can be transported over network and started on another 
# metadata service container.

"""
export_data -c container-1
export_data -o <output-filename> -c container-1
export_data -o <output-filename> -l <output-location> -c container-1
"""

import optparse
import os
import subprocess
import re
       
def main():
  p = optparse.OptionParser()
  p.add_option('--container', '-c', default="container")
  p.add_option('--output', '-o', default="exported.tar")
  p.add_option('--location', '-l', default="/opt/")
  options, arguments = p.parse_args()
  print 'Exporting data from %s ' % options.container
  print 'To location %s%s ' % (options.location, options.output)

  os.system('docker export -o %s%s %s' % (options.location, options.output, options.container))

if __name__ == '__main__':
  main()
