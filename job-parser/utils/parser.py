from bs4 import BeautifulSoup
import requests
from datetime import date

def rawDateToDateTime(raw_date):
   raw_date_arr = raw_date.split("/")
   for i, interval in enumerate(raw_date_arr):
        raw_date_arr[i] = int(interval)

   return date(raw_date_arr[2], raw_date_arr[0], raw_date_arr[1]).isoformat()

class Company:
   def __init__(self, name, link='', locations=[],
                positions=[], requires_citizenship=False, posted_date=None):
       self.name = name
       self.link = link
       self.locations = locations
       # tuple of postiion name, position link
       self.positions = positions
       self.requires_citizenship = requires_citizenship
       self.posted_date = posted_date

def parseCompanyListing(link):
    html_document = requests.get(link).text
    soup = BeautifulSoup(html_document, 'html.parser')

    # This only works because the only table is the company lists
    company_list = soup.find_all('tr')
    # remove table headers
    company_list.pop(0)
    companies = []
    for company_tag_listing in company_list:
        # html listing as <td> element
        listing = company_tag_listing.find_all('td')
        company_name, company_link = (listing[0].string,
                                      listing[0].a.get('href')[2:-2])

        locations = []
        dirty_locations = listing[1].get_text().split('-')
        if len(dirty_locations) > 1:
            # skip empty location from delimiter
            for location in dirty_locations[1:]:
                locations.append(str(location.strip()))
        else:
            locations = dirty_locations

        roles = []
        role_html = listing[2].find_all('a')
        for role in role_html:
            # invalid url, potentially do something to mark these as closed in the future
            role_link = role.get('href')[2:-2]
            if role_link == '/ReaVNaiL/New-Grad-2024/blob/main':
                continue
            roles.append((str(role.string), str(role_link)))

        if len(roles) == 0:
            continue

        raw_date_added = listing[4].string
        date_added = None
        if raw_date_added:
            date_added = rawDateToDateTime(raw_date_added)

        company = Company(str(company_name), str(company_link), locations, roles, False, date_added)
        companies.append(company)

    return companies

# print to file
# companies = parseCompanyListing('https://github.com/ReaVNaiL/New-Grad-2024')
#
# with open('companies.txt', 'w') as file:
#     for company in companies:
#         positions = ""
#         for position in company.positions:
#             positions += position[0] + '(' + position[1] + ')' + ", "
#         positions = positions[:-1]
#         file.write(company.name + ' | ' + company.link + ' | ' + positions + ' | ' + company.posted_date + "\n")

