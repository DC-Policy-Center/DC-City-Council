# DC City Council
We will fill this folder with DC City Council relevant code and data.  



## Current files in repository
|File Name             | Description|
|:---------------------|:--------------|
|dcLeg.py              |Early python script used to interact with the DC LIMS API|
|committeeScrape.py    |Python Script used to pull committee members and their contact information from the DC Committee Websites|
|newLegislationPull.py|This will call the DC LIMS API for all legislation from the 22nd council period, for each item it does a secondary call for details:introducer.  It outputs a .csv file of legislation.  !!!WARNING!!! High number of API calls, use infrequently|
|dcLegislation.py|Early framework for API helper|
|dclims.json| Output json file from dcLeg.py|
|New Legislation.csv|Final output file from newLegislationPull.py|
|Saved New Legislation Folder| Folder to contain saved output csv files from newLegislationPull.py|
|Saved New Legislation/New Legislation as of 3_28_17.csv|Frozen/saved output file from newLegislationPull.py|
|Saved New Legislation/New Legislation as of 3_29_17.csv|Frozen/saved output file from newLegislationPull.py|
