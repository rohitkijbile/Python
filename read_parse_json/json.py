import json

# Open and read the JSON file
with open('data.json', 'r') as file:
    data = json.load(file)

# Access data
print("Full data:", data)
print("Id:", data.get("Id"))
print("Name:", data.get("Name"))
print("Skills:", data.get("Skills"))
print("Location:", data.get("Details", {}).get("Location"))
