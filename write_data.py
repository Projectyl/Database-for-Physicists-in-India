import json
import os
import yaml

categories = json.load(open("./info_files/category_file.json", 'r'))
headings = json.load(open('./info_files/headings.json' ,'r'))
folder = './institute_data/'
cat_folder = "./category_data/"
if not os.path.exists(cat_folder): os.mkdir(cat_folder)

files = [folder+insti+".json" for insti in json.load(open('./info_files/institutes.json', 'r'))]
cat_data = {}
for key in categories:
    cat_data[key] = []
    
for file in files:
    data = json.load(open(file, 'r'))
    for prof in data:
        for key,val in categories.items():
            if True in [interest.lower() in val for interest in prof[headings[3]]]: cat_data[key].append(prof)
poppable_id = []
for other_prof in reversed(cat_data['Others']):
    if other_prof in [prof for cat, profs in cat_data.items() for prof in profs if cat != 'Others']:
        cat_data['Others'].remove(other_prof)

for key in cat_data:
    if len(cat_data[key]) == 0:
        continue
    json.dump(cat_data[key], open(cat_folder+key+'.json', 'w'))
