import yaml
import os

category_file = "./category_file.yml"
all_cat_file = "./all_cats.txt"
if not os.path.exists(all_cat_file): os.mknod(all_cat_file)
try:
    all_cats = yaml.safe_load(open(category_file, 'r')).values()
except:
    all_cats = []
subcats = []
for cat in all_cats:
    subcats += cat
[open(all_cat_file, 'a').write(subcat+'\n') for subcat in subcats]