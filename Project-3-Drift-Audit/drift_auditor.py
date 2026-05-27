import json

# Load both configurations
with open('config_staging.json', 'r') as f1:
    staging = json.load(f1)

with open('config_production.json', 'r') as f2:
    production = json.load(f2)

print("--- RUNNING ENVIRONMENT DRIFT AUDIT ---")

# Find keys that are in staging but missing in production
for key in staging:
    if key not in production:
        print(f"🚨 CONFIGURATION DRIFT DETECTED: Feature '{key}' is active in Staging but MISSING in Production!")
    else:
        print(f"✅ Match: '{key}' configuration is aligned across environments.")

print("--- DRIFT AUDIT COMPLETE ---")