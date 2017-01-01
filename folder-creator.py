import os
import json

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

with open("./CCSS/data.json") as f:
    data = json.load(f)

def create_subdirs(base_dir, data):
    f = open(base_dir + "/data.json", "w")
    f.write(json.dumps(data))
    f.close()
    for child in data["children"]:
        mkdir(base_dir + "/" + child["standard_slug"])
        create_subdirs(base_dir + "/" + child["standard_slug"], child)

create_subdirs("./CCSS", data)
