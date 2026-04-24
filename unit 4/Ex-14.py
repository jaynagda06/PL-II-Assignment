import csv
import json

with open('data.csv', 'r') as csv_file:
    csv_reader = csv.DictReader(csv_file)
    
    
    data = list(csv_reader)

with open('data.json', 'w') as json_file:
    json.dump(data, json_file, indent=4)

print("CSV converted to JSON successfully!")