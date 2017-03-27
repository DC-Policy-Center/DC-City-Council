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
import requests, json, pprint, pandas, csv
#Building Request
rowLimit = '100'                               #seems to be the max limit
offSet = 0                                     #will change to string in the URI
q = {"CouncilPeriod": "22"}                    #Sets advanced search query to search for current council period (22)
head = {'content-type':'application/json'}     #Requests JSON response

#Building API call from request building
website = 'http://lims.dccouncil.us/api/v1/'+'Legislation/AdvancedSearch?%s'%(rowLimit)

#Sending POST request
response = requests.post(website,data=json.dumps(q),headers=head)

data_json = response.json()


with open('newLegislation.json','w') as f:
    toWrite = json.dumps(response.json())
    pprint.pprint(toWrite,f)
f.close()

dataHeaders = ['Id','CouncilPeriod','ShortTitle','LegislationNumber','LawNumber','ActNumber',
'IntroductionDate','Modified',' CommitteeReferral',
'CommitteeReferralComments',
  'Deemed','DeemedOn','LegislationStatus','Category'
  ,'Subcategory','DocumentUrl']

csvHeader = [] #Initialize empty list for headers for CSV writing
with open('output.csv','w', newline='',encoding='utf-8') as f:
    csvWriter = csv.writer(f)
    for key, value in data_json[0].items():
        csvHeader.append(key)
    csvWriter.writerow(csvHeader)
    for i in range(len(data_json)):
        row = []
        for key, value in data_json[i].items():
            row.append(value)
        csvWriter.writerow(row)
        #pprint.pprint(data_json[i]['LegislationNumber'],f)
f.close()

df = pandas.read_csv('output.csv',encoding='utf-8')
df = df.sort_values(by='Id',ascending=False)
df.to_csv('output_2.csv', index=False, columns=dataHeaders)
