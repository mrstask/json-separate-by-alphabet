import json


new_dict = {}


with open('cities.json', 'r') as f:
    cities = json.loads(f.read())
for some in cities:
    if some['name'][0].lower() not in new_dict.keys():
        new_dict[some['name'][0].lower()] = [some]
    else:
        new_dict[some['name'][0].lower()].append(some)


for key, value in new_dict.items():
    with open('jsons/'+key+'.json', 'w') as f:
        json.dump(new_dict[key], f)
