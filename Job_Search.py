import urllib.request
from bs4 import BeautifulSoup as soup
import re

jobs_url = "http://www.naukri.com/machine-learning-jobs"
req = urllib.request.Request(jobs_url, headers={'User-Agent': 'Mozilla/5.0'})

#opening connection and grabbing the page
uClient = urllib.request.urlopen(req)
page_html = uClient.read()
uClient.close()

#html parsing
page_soup = soup(page_html, "html.parser")

#grab all divs with a class of result
results = page_soup.findAll("div", {"type": "tuple"})

filename = "jobs.csv"
f = open(filename, "w")

headers = "Title, Company, Location, Summary, Experience, Link \n"

f.write(headers)

for result in results:
    title_code = result.findAll('li', {'class':'desig'})
    title = title_code[0].text.strip()

    company = result.findAll('span', {'class':'org'})
    company_name = company[0].text.strip()

    location = result.findAll('span', {'class':'loc'})
    location_name = location[0].text.strip()

    summary = result.findAll('span', {'class':'desc'})
    if(len(summary) > 0) :
        job_summary = summary[0].text.strip()
    else :
        job_summary = 'Not Available'

    exp = result.findAll('span', {'class':'exp'})
    experience = exp[0].text.strip()

    job_link = result.a['href']
    
    print (title)
    print (company_name)
    print (location_name)
    print (job_summary)
    print (experience)
    print (job_link)

    f.write(title + "," + company_name + "," + location_name + "," + job_summary + "," + experience + "," + job_link + "\n")

f.close()