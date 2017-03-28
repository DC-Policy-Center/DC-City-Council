#Begin intro comments
'''
Dependencies: NONE;
API help from DC Council Website:http://lims.dccouncil.us/api/Help
newLegislationPull.py is utilizes the advanced search feature in the LIMS API
specifically to request details on all the legislation from the current (22)
council period.

|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|
'''
#End of intro comments
#Requests for POST call, json for parsing, pprint for pretty print outputs, pandas for database, csv for csv writing
import requests, json, pprint, pandas, csv, dcLegislation, os
#Building Request
verbose = True
rowLimit = '100'                               #seems to be the max limit
offSet = 0                                     #will change to string in the URI
q = {"CouncilPeriod": "22"}                    #Sets advanced search query to search for current council period (22)
head = {'content-type':'application/json'}     #Requests JSON response


csvHeader = []
csvHeader.append('Introducer') #Initialize empty list for headers for CSV writing
dataHeaders = [     'Id','CouncilPeriod','ShortTitle','Introducer',
                    'LegislationNumber','LawNumber','ActNumber',
                    'IntroductionDate','Modified','CommitteeReferral',
                    'CommitteeReferralComments','Deemed','DeemedOn',
                    'LegislationStatus','Category','Subcategory','DocumentUrl']
introducerException = 0





#Building API call from request building

website = 'http://lims.dccouncil.us/api/v1/'+'Legislation/AdvancedSearch?%s'%(rowLimit)
if(verbose):print('Website: '+website)

#Sending POST request
if(verbose):print('\nRequest sent...')
response = requests.post(website,data=json.dumps(q),headers=head)
data_json = response.json()

if(verbose):print('\nCreating JSON file...')
with open('newLegislation.json','w') as f:
    toWrite = json.dumps(response.json())
    pprint.pprint(toWrite,f)
f.close()
if(verbose):print('\nJSON file done...')




if(verbose):print('\nCreating CSV file...')
with open('tmp.csv','w', newline='',encoding='utf-8') as f:
    csvWriter = csv.writer(f)
    for key, value in data_json[0].items():
        csvHeader.append(key)
    csvWriter.writerow(csvHeader)
    for i in range(len(data_json)):
        #if(verbose):print('\n!!! Processing Legislation number:%i of %i'%(i,len(data_json)))
        LN = data_json[i]['LegislationNumber']               # LN: Legislation Number
        LND = dcLegislation.apiCalls.getDetails(LN)          # LND; Legislation Number Details
        jLND = LND.json()                                    # jLND: JSON format of Legislation Number Details
        try:
            introducer = jLND['Legislation']['Introducer']   # The introducer of the legislation
        except:
            introducer = 'NONE'    #Some pieces of legislation have no introducer

        row = []
        row.append(introducer)
        for key, value in data_json[i].items():
            row.append(value)
        csvWriter.writerow(row)
        #pprint.pprint(data_json[i]['LegislationNumber'],f)
f.close()
if(verbose):print('\nCSV file done...')




if(verbose):print('\nBuilding dataframe...')
df = pandas.read_csv('tmp.csv',encoding='utf-8')
df = df.sort_values(by='Id',ascending=False)
if(verbose):print('\nWriting dataframe to CSV file...')
df.to_csv('New Legislation.csv', index=False, columns=dataHeaders)

print('Cleaning up directory...')
os.remove('newLegislation.json')
os.remove('tmp.csv')
