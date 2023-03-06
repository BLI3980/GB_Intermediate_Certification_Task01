import json

data = {
    "president": {
        "name": "Zaphod Beeblebrox",
        "species": "Betelgeusian"
    }
}

with open("data_file.json", "w") as write_file:
    json.dump(data, write_file)
    json_string = json.dumps(data, indent=2)

print(json_string)


with open("data_file.json", "r") as read_file:
    data = json.load(read_file)

print(data)