#Begin intro comments
'''
Dependencies: NONE;
API help from DC Council Website:http://lims.dccouncil.us/api/Help


|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|
'''
#End of intro comments
import requests, json, pprint, pandas
gOp = 'GET'
rowLimit = '100' #seems to be the max limit
offSet = 0 #will change to string in the URI
councilPeriod = '22'
legislationNumber = 'IG22-0013'


#Legislation
sL_LL ='Legislation/LatestLaws?%s'%(rowLimit)
sL_LN ='Legislation/Details?legislationNumber=%s'%(legislationNumber) #GET
sL_AS ='Legislation/AdvancedSearch?%s'%(rowLimit) #POST

#Voting
s_V ='Voting/Search?rowLimit=%s&offSet=%i&SearchCriteria'%(rowLimit,offSet)
#Master
sM_CP = 'masters/Members?councilPeriod=%s'%councilPeriod
sM_LS ='masters/LegislationStatus'
searchType = sL_LN

q = {
 }
'''
q ={
"CouncilPeriod": "22"
    "StartDate":"2010-01-01",
    "EndDate":"2017-02-17"

}
'''

head = {'content-type':'application/json'}

website = 'http://lims.dccouncil.us/api/v1/'+searchType
print('\n\nWebsite:'+website)

if gOp == 'GET':
    response = requests.get(website,data=json.dumps(q),headers=head)
elif gOp == 'POST':
    response = requests.post(website,data=json.dumps(q),headers=head)

try:
    print(response.text)
except:
    pass
data_json = response.json()


with open('dclims.json','w') as f:
    toWrite = json.dumps(response.json())
    pprint.pprint(toWrite,f)
f.close()
index = 0

for leg in data_json:
    #print(data_json[index]['DateOfVote'])
    index+=1

print(index)


with open('output.txt','w') as f:
    pprint.pprint(data_json[0].keys(),f)
    for i in range(len(data_json)):
        pprint.pprint(data_json[i]['LegislationNumber'],f)
f.close()
