import json

# Read the raw line-delimited JSON objects
with open("data/world_bank_data.json", "r") as f:
    lines = f.readlines()

# Parse each line into a JSON object
parsed = [json.loads(line) for line in lines]

# Save it as a proper JSON array
with open("data/world_bank_data_fixed.json", "w") as f:
    json.dump(parsed, f, indent=2)

print("✅ Converted raw JSON to valid JSON array.")
