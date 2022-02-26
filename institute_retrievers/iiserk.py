from bs4 import BeautifulSoup
import requests
import json
from tqdm import tqdm
import os
import time

headings = json.load(open('../info_files/headings.json' ,'r'))
folder = '../institute_data/'
if not os.path.exists(folder): os.mkdir(folder)

url = "https://www.iiserkol.ac.in/web/en/people/faculty/dps/#gsc.tab=0"
soup = BeautifulSoup(requests.get(url).content, features='lxml')
prof_details = []
for tag in tqdm(soup.findAll('b', text="Department:"), desc="IISER K"):
    parent = tag.findPrevious('td')
    name = parent.findChild('a', attrs={'style':"color:#0976e4;"}).text.strip()
    desig = parent.findChild('b', text="Department:").findPrevious().previousSibling.strip()
    try:
        interests_string = parent.findChild('b', text="Research Area:").nextSibling
        delim = ';' if ';' in interests_string else ','
        interests = [s.strip() for s in interests_string.split(delim)]
    except:
        interests = []
    homepage = "https://www.iiserkol.ac.in" + tag.findPrevious('a')['href']
    email = parent.findChild('b', text="Email:").nextSibling.replace(' [AT] ', '@')
    prof_details.append({headings[0]: name, headings[1]: "IISER Kolkata", headings[2]: desig, headings[3]: interests, headings[4]: homepage, headings[5]: email})
    time.sleep(0.5)

json.dump(prof_details, open(folder+'iiserk.json', 'w'))
