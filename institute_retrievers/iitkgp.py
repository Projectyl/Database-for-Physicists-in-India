from bs4 import BeautifulSoup
import requests
import csv
from tqdm import tqdm
import os
import time

headings = open('../headings.txt' ,'r').read().strip().split('\n')
folder = '../institutes/'
if not os.path.exists(folder): os.mkdir(folder)
csv.writer(open(folder+'iitkgp.csv', 'w'), delimiter='\t').writerow(headings)
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
        prof_dict = []
        for k in j.findChildren('h3'):
            prof_dict.append(k.text.strip()) #Get name of professor
            prof_dict.append('IIT Kharagpur')
            prof_dict.append(k.findNext('span').findNext('span').text.split('\n')[1].strip())
        for l in j.findChildren('blockquote', attrs = {'class':'blockquote'}):
            prof_dict.append([i.text.replace('\xa0','').strip() for i in l.findChildren('li')])  #Get the research areas
        prof_page = base_url+j.findNext('a')['href'].split(';')[0]
        prof_dict.append(prof_page) #Get the contact detail of the Professor
        prof_soup = BeautifulSoup(requests.get(prof_page).text, 'html.parser')
        prof_dict.append(prof_soup.find('div', attrs = {'class':'accordion-contact-list'}).findChild('li').text.strip()) #Get the contact detail of the Professor
        prof_details.append(prof_dict) 
        time.sleep(0.5)
        break
csv.writer(open(folder+'iitkgp.csv', 'a'), delimiter='\t').writerows(prof_details)
