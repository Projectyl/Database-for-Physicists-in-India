from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm
import os
import time

headings = json.load(open('../info_files/headings.json' ,'r'))
folder = '../institute_data/'
if not os.path.exists(folder): os.mkdir(folder)

#Get the faculty page using requests
page = requests.get('http://www.iitkgp.ac.in/department/PH/faculties')
#Parse it using Beautiful Soup
soup = BeautifulSoup(page.text, 'html.parser')
prof_details = []
#Scraping code
block = soup.find_all('div', attrs = {'class':'col-lg-12'})[2]
base_url = 'http://www.iitkgp.ac.in'
for i in tqdm(block.findChildren('div', attrs = {'class':'col-lg-12'}), desc="IIT KGP"):
    for j in i.findChildren('div', attrs = {'class':'row'}):
        prof_dict = {}
        for k in j.findChildren('h3'):
            prof_dict[headings[0]] = k.text.strip() #Get name of professor
            prof_dict[headings[1]] = 'IIT Kharagpur'
            prof_dict[headings[2]] = k.findNext('span').findNext('span').text.split('\n')[1].strip()
        for l in j.findChildren('blockquote', attrs = {'class':'blockquote'}):
            prof_dict[headings[3]] = [i.text.replace('\xa0','').strip() for i in l.findChildren('li')]  #Get the research areas
        prof_page = base_url+j.findNext('a')['href'].split(';')[0]
        prof_dict[headings[4]] = prof_page #Get the contact detail of the Professor
        prof_soup = BeautifulSoup(requests.get(prof_page).text, 'html.parser')
        prof_dict[headings[5]] = prof_soup.find('div', attrs = {'class':'accordion-contact-list'}).findChild('li').text.strip() #Get the contact detail of the Professor
        prof_details.append(prof_dict) 

        time.sleep(0.5)
        break

json.dump(prof_details, open(folder+'iitkgp.json', 'w'))
