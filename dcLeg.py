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

rowLimit = '100' #seems to be the max limit
offSet = 0 #will change to string in the URI
s_V ='Voting/Search?rowLimit=%s&offSet=%i&SearchCriteria'%(rowLimit,offSet)
searchType = s_V

q = {}
'''
q ={

    "StartDate":"2010-01-01",
    "EndDate":"2017-02-17"

}
'''

head = {'content-type':'application/json'}

website = 'http://lims.dccouncil.us/api/v1/'+searchType
print('\n\nWebsite:'+website)
response = requests.post(website,data=json.dumps(q),headers=head)
print(response.text)
data_json = response.json()


with open('dclims.json','a') as f:
    toWrite = json.dumps(response.json())
    pprint.pprint(toWrite,f)
f.close()
index = 0

for leg in data_json:
    #print(data_json[index]['DateOfVote'])
    index+=1

print(index)
