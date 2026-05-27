import json  # This tells Python to load the tools needed to read JSON files

# 1. Open and load your configuration file
with open('routing_config.json', 'r') as file:
    config_data = json.load(file)

print("--- STARTING CONFIGURATION AUDIT ---")
print(f"Checking environment: {config_data['environment']}")

# 2. Extract the routing rules so we can test them
rules = config_data['routing_rules']

# 3. Apply the Business Logic (The Test)
# A configuration analyst wants to ensure max_retries is never 0, or messages will fail too easily!
if rules['sms_max_retries'] > 0:
    print("✅ SUCCESS: 'sms_max_retries' configuration is valid and safe.")
else:
    print("❌ ERROR: 'sms_max_retries' cannot be 0. System will fail to resend dropped messages.")

print("--- AUDIT COMPLETE ---")