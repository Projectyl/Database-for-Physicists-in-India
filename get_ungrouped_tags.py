#!/bin/python
import json
import os

category_file = "./info_files/category_file.json"
grouped_tags_file = "./info_files/grouped_tags.json"
headings = json.load(open('./info_files/headings.json' ,'r'))
institutes_files = ['./institute_data/'+file for file in os.listdir('./institute_data/')]
ungrouped_tags_file = "./info_files/ungrouped_tags.json"
grouped_tags = [tag for tags in json.load(open(category_file, 'r')).values() for tag in tags]
ungrouped_tags = []

for file in institutes_files:
    data = json.load(open(file, 'r'))
    for prof in data:
        ungrouped_tags += [interest.lower() for interest in prof[headings[3]] if interest.lower() not in grouped_tags and interest != ""]
json.dump(ungrouped_tags, open(ungrouped_tags_file, 'w'))
