import os
import glob
import sys

from normalize import normalize

# Grab all csv filenames from current directory
# NOTE: Can change variables to sys args
path = '.'
extension = 'csv'
result = glob.glob('*.{}'.format(extension))

# NOTE: This is static for example purposes; should change to make scriptable
column_name = sys.argv[1]

for csv in result:
    normalize(csv, column_name)