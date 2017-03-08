'''
committeeScrape.py is used to scrape the static DC Gov committee webpages for
the staff contact information.
Libraries Used: Requests, bs4


|Signature-------------------------------------------|
|Written for DC Policy Center by Michael Watson; 2017|
|www.DCPolicyCenter.org / DC-Policy-Center.github.io |
|github:M-Watson & MW-DC-Policy-Center               |
|----------------------------------------------------|
'''

import requests                      #Used for requesting html data
from bs4 import BeautifulSoup as BS  #Used for parsing HTML Tags

#Chose the committee you would like to pull contacts from
committee = 'committe_on_housing_and_neighborhood_revitalization'
verbose = 'no' #Verbose mode is used to print out statements about the actions taking place in the program.  Use 'yes' or 'no'

#Setting variables that can be initialized early
fileName = committee + '.txt'  #filemame of file written, created from committee choice
name = []  #Name from pulled data
pos = []   #Position from pulled data
phone = []  #Phonenumber from pulled data
email = []  #e-mail address from pulled data
rows_to_write_list = []  #A list of concatenated strings that will make up the row to be written to a file

#


#Links to committee websites
committee_websites_dict={
    'committe_on_housing_and_neighborhood_revitalization' :      'http://dccouncil.us/committees/committee-on-housing-and-neighborhood-revitalization',
    'committe_on_business_and_economic_development'       :      'http://dccouncil.us/committees/committee-on-business-and-economic-development',
    'committee_of_the_whole'                              :      'http://dccouncil.us/committees/committee-of-the-whole',
    'committee_on_education'                              :      'http://dccouncil.us/committees/committee-on-education',
    'committee_on_finance_and_revenue'                    :      'http://dccouncil.us/committees/committee-on-finance-and-revenue',
    'committee_on_government_operations'                  :      'http://dccouncil.us/committees/committee-on-government-operations',
    'committee_on_health'                                 :      'http://dccouncil.us/committees/committee-on-health',
    'committee_on_human_services'                         :      'http://dccouncil.us/committees/committee-on-human-services',
    'committee_on_the_judiciary_and_public_safety'        :      'http://dccouncil.us/committees/committee-on-the-judiciary-and-public-safety',
    'committee_on_transportation_and_the_enviroment'      :      'http://dccouncil.us/committees/committee-on-transportation-and-the-environment',
    'committee_on_labor_and_workforce_development'        :      'http://dccouncil.us/committees/committee-on-labor-and-workforce-development'
}#END OF committee_website_dict


page_n = committee_websites_dict[committee] #Setting the website to pull information from
if(verbose=='yes'):print('\nRequesting html from: \n'+'Committee: '+str(committee)+'\nURL: '+ page_n+'\n...')



#Website request section
page_html = requests.get(page_n)                         #Requesting data from stated website for committee
page_bs = BS(page_html.text,'lxml')                      #parsing data pulled from website

staff = page_bs.find_all("div",class_="staff-entry")    #Searching through parsed data for staff-entry class, this class contains contact information

if(verbose=='yes'):print('\nBeginning to build contact information from parsed data...')
index_of_row = 0                            #This index is to show how many members have been created
for member_card in staff:                   #The member card is one chunck of data including all the contact information
    index_of_staff_member_data = 0          #This index iterates through staff member data to choose what type of information is being collected
    for section in member_card:             #The section breaks the member_card up into usable chunks of data
        for item in section:                #The item as it is iterated through the section
############  IF LOGIC: This logic is currently hardcoded to specific locations
###########   The ideal situation would be using something like regular expressions to find the information desired
            if index_of_staff_member_data == 1:  # Data pulled has an extra empty space located at index[0], making the name index[1]
                name.append(str(item))
            elif index_of_staff_member_data == 3:
                pos.append(str(item))
            elif index_of_staff_member_data == 5:
                phone.append(str(item))
            elif index_of_staff_member_data == 7:
                email.append(str(item))
            index_of_staff_member_data +=1
    row_to_write = name[index_of_row] + ',' + pos[index_of_row] + ',' + phone[index_of_row] + ',' + email[index_of_row] + '\n'
    index_of_row+=1
    rows_to_write_list.append(row_to_write)


################ Writing contact information to a file named after the committee #############
if(verbose=='yes'):print('\nBeginning to write contact information to: '+ str(fileName)+'.txt\n...')
with open(fileName,'w')  as f:
    for line in rows_to_write_list:
        f.write(line)
if(verbose=='yes'):print('\nCompleted writing contact information to: '+ str(fileName)+'.txt\n---END---')

################################################################################
###################### END OF committeeScrape.py script ########################
################################################################################
'''                     Apendicies
Dependencies: NONE
Flow Chart:
User -input->  committeeScrape.py -output-> [committee].txt


                       END Apendicies'''
