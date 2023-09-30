from bs4 import BeautifulSoup
import requests
import re

html_document = requests.get('https://github.com/ReaVNaiL/New-Grad-2024').text
soup = BeautifulSoup(html_document, 'html.parser')
#print(soup.tr)
#print(soup.find_all('tr')[2])
#company_list = soup[:1]
#print(company_list)
class Company:
   def __init__(self, company_name, company_link='', locations=[],
                position_name=[], position_link=[], posted_date=None):
       self.company_name = company_name
       self.company_link = company_link
       self.locations = locations
       self.position_name = position_name
       self.position_link = position_link
       self.posted_date = posted_date
# This only works because the only table is the company lists
company_list = soup.find_all('tr')
# remove table headers
company_list.pop(0)
companies = []
for company_tag_listing in company_list:
    listing = company_tag_listing.find_all('td')
    # print(listing[0])
    company_name, company_link = (listing[0].string,
                                  listing[0].a.get('href'))
    print(company_name, company_link)

    locations = []
    dirty_locations = listing[1].get_text().split('-')
    if len(dirty_locations) > 1:
        # skip empty location from delimiter
        for location in dirty_locations[1:]:
            locations.append(location.strip())
    else:
        locations = dirty_locations
    # print(locations)



