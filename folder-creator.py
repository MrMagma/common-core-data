import os
import json

def mkdir(dirname):
    if not os.path.exists(dirname):
        os.makedirs(dirname)

with open("./CCSS/data.json") as f:
    data = json.load(f)

def write_children(base_dir, data):
    children = []
    
    for child in data["children"]:
        child2 = {}
        for key in child:
            if key == "children":
                child2[key] = len(child[key])
            else:
                child2[key] = child[key]
        children.append(child2)
    
    f = open(base_dir + "/children.json", "w")
    f.write(json.dumps(children))
    f.close()

def create_subdirs(base_dir, data):
    f = open(base_dir + "/data.json", "w")
    f.write(json.dumps(data))
    f.close()
    
    write_children(base_dir, data)
    
    for child in data["children"]:
        mkdir(base_dir + "/" + child["standard_slug"])
        create_subdirs(base_dir + "/" + child["standard_slug"], child)

create_subdirs("./CCSS", data)
