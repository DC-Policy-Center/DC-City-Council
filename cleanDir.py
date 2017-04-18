''' Specific use case python script to clean the DC-City-Council Folder
from temporary files produced through:

- newLegislationPull.py
    * newLegislation.json
    * tmp.csv
'''
import os                               # Importing os to delete files in directory

# Files produced from newLegislation.py
os.remove('newLegislation.json')
os.remove('tmp.csv')
