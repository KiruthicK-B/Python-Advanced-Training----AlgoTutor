import json

with open('Food_Delivery_Route_Efficiency_Dataset.json', 'r') as f:
    data = json.load(f)

print(data[3])

print("length of data:", len(data))

list = [10, 20, 30, 40, 50]

list_json = json.dumps(list)
print("JSON list:", list_json)
print("Type of JSON list:", type(list_json))