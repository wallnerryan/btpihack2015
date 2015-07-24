!/usr/bin/env python

# This exports the metadata container and saves it to a .tar file.
# The TAR file can be transported over network and started on another 
# metadata service container.

"""
export_data -c container-1
export_data -o <output-filename> -c container-1
export_data -o <output-filename> -l <output-location> -c container-1
"""
