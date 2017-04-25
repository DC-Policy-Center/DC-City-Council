''' Specific use case python script to clean the DC-City-Council Folder
from temporary files produced through:

- newLegislationPull.py
    * newLegislation.json
    * tmp.csv
'''
import os                               # Importing os to delete files in directory

# Files produced from newLegislation.py
try:os.remove('newLegislation.json')
except:pass

try:os.remove('tmp.csv')
except:pass
