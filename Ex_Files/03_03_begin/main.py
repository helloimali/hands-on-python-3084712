import csv
import json
from pprint import pprint

EINSTEIN = {
    "birthplace": "Germany",
    "name": "Albert",
    "surname": "Einstein",
    "born": "1879-03-14",
    "category": "physics",
    "motivation": "for his services to Theoretical Physics...",
}
# convert to json
einstein_json = json.dumps(EINSTEIN) 
# convert json to dict
back_to_dict = json.loads(einstein_json)

print(einstein_json)
pprint(back_to_dict)

with open("laureates.csv", "r") as f:
    reader = csv.DictReader(f)
    laureates = list(reader)

# open a new file in write mode
with open("laureates.json", "w") as f:
    # write into file, file does not have to exist
    json.dump(laureates, f, indent=2)
