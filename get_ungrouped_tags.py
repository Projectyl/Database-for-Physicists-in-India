import json

headings = json.load(open('./info_files/headings.json' ,'r'))
institutes_files = ['./institute_data/'+insti+'.json' for insti in json.load(open('./info_files/institutes.json', 'r'))]
ungrouped_tags_file = "./info_files/ungrouped_tags.json"
existing_tags = json.load(open('./info_files/grouped_tags.json', 'r'))
ungrouped_tags = []

for file in institutes_files:
    data = json.load(open(file, 'r'))
    for prof in data:
        ungrouped_tags += [interest.lower() for interest in prof[headings[3]] if interest.lower() not in existing_tags and interest != ""]
json.dump(ungrouped_tags, open(ungrouped_tags_file, 'w'))
