import json
import os
import yaml

category_file = "./category_file.yml"
headings = open('headings.txt' ,'r').read().strip().split('\n')
folder = './institutes/'
cat_folder = "./category_data/"
if not os.path.exists(cat_folder): os.mkdir(cat_folder)

files = [folder+insti+".json" for insti in open('institutes.txt', 'r').read().strip().split('\n')]
cat_data = {}
for key in yaml.safe_load(open(category_file, 'r')):
    cat_data[key] = []
    
for file in files:
    data = json.load(open(file, 'r'))
    for prof in data:
        for key,val in yaml.safe_load(open(category_file, 'r')).items():
            if True in [interest.lower() in val for interest in prof[headings[3]]]: cat_data[key].append(prof)
            
for key in cat_data:
    print (cat_data[key])
    if len(cat_data[key]) == 0:
        continue
    json.dump(cat_data[key], open(cat_folder+key+'.json', 'w'))