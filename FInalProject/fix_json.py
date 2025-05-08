import json

with open("data/world_bank_data.json", "r") as f:
    lines = f.readlines()

parsed = [json.loads(line) for line in lines]

with open("data/world_bank_data_fixed.json", "w") as f:
    json.dump(parsed, f, indent=2)

print("✅ Converted raw JSON to valid JSON array.")
