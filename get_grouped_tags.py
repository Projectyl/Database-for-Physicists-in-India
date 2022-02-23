import json
import os

category_file = "./info_files/category_file.json"
existing_tags_file = "./info_files/grouped_tags.json"
existing_tags = [tag for tags in json.load(open(category_file, 'r')).values() for tag in tags]
json.dump(existing_tags, open(existing_tags_file, 'w'))
