import json

ungrouped_tags_file = "./info_files/ungrouped_tags.json"
category_file = "./info_files/category_file.json"
existing_tags_file = "./info_files/grouped_tags.json"

categories = json.load(open(category_file, 'r'))
ungrouped_tags = json.load(open(ungrouped_tags_file, 'r'))
text = '\n'.join([str(i+1) + ". " + j for i,j in enumerate(categories.keys())])+'\nXX\n'
for tag in ungrouped_tags:
    if tag == "":
        continue
    ch = input(tag+'\n\n'+text)
    if ch == 'XX':
        print ("Breaking")
        break
    if ch.isdigit():
        loc = int(ch) - 1
        categories[list(categories.keys())[loc]].append(tag)
    else:
        categories[ch] = [tag]
    text = '\n'.join([str(i+1) + ". " + j for i,j in enumerate(categories.keys())])+'\nXX\n'
    ungrouped_tags.remove(tag)

json.dump(categories, open(category_file, 'w'))
json.dump(ungrouped_tags, open(ungrouped_tags_file, 'w'))
existing_tags = [tag for tags in json.load(open(category_file, 'r')).values() for tag in tags]
json.dump(existing_tags, open(existing_tags_file, 'w'))
