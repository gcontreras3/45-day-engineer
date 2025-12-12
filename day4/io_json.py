import json

data = {
    "users": [
        {"name": "Alice", "age": 25},
        {"name": "Bob", "age": 30}
    ]
}

with open("sample.json", "w") as f:
    json.dump(data, f, indent=4)
with open("sample.json", "r") as f:
    loaded_data = json.load(f)
print(loaded_data)