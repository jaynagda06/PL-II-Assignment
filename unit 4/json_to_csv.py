import json, csv

with open("data.json") as f:
    data = json.load(f)

with open("data.csv", "w", newline="") as f:
    writer = csv.DictWriter(f, fieldnames=data[0].keys())
    writer.writeheader()
    writer.writerows(data)