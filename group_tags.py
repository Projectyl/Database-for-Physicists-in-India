#!/bin/python
import os
import json
import subprocess

category_file = "./info_files/category_file.json"
ungrouped_tags_file = "./info_files/ungrouped_tags.json"
ungrouped_tags = json.load(open(ungrouped_tags_file, 'r'))
categories = json.load(open(category_file ,'r'))

classes = []
for tag in ungrouped_tags:
    print (tag)
    [print (i+1,category) for i,category in enumerate(categories.keys())]
    choice = int(input())
    if choice < 1:
        continue
    cat = list(categories.keys())[choice-1]
    classes.append((tag, cat))

tmp_file = "./info_files/tmp_file.txt"
[open(tmp_file,'a').write('\t'.join(class_i)+'\n') for class_i in classes]
process = subprocess.Popen(['vim', tmp_file])
process.wait()
classes = [line.strip().split('\t') for line in open(tmp_file,'r').readlines()]
os.remove(tmp_file)
for tag,class_i in classes:
    categories[class_i].append(tag)
json.dump(categories, open(category_file, 'w'))
