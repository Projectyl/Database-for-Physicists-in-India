import json

headings = open('headings.txt' ,'r').read().strip().split('\n')
folder = './institutes/'
files = [folder+insti+".json" for insti in open('institutes.txt', 'r').read().strip().split('\n')]
new_cat_file = "./new_cats.txt"
open(new_cat_file, 'w')
try:
    all_cat_file = "./all_cats.txt"
    all_subcats = open(all_cat_file, 'r').read().strip().join('\n')
except:
    all_subcats = []

for file in files:
    data = json.load(open(file, 'r'))
    for prof in data:
        [open(new_cat_file, 'a').write(interest.lower()+'\n') for interest in prof[headings[3]] if interest.lower() not in all_subcats]
