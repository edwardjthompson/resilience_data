import os
import glob

from em_diff import em_diff

# Grab all csv filenames from current directory
# NOTE: Can change variables to sys args
path = '.'
extension = 'csv'
result = glob.glob('*.{}'.format(extension))

for csv in result:
    em_diff(csv)