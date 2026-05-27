import json

# Load the user data
with open('user_payload.json', 'r') as file:
    users = json.load(file)

print("--- STARTING DATABASE SCHEMA VALIDATION ---")

# Check each user record
for user in users:
    name = user['name']
    country_code = user['phone_country_code']
    
    # Check if country code is a number (integer)
    if isinstance(country_code, int):
        print(f"✅ PASS: {name}'s profile layout is correct.")
    else:
        print(f"❌ FAIL: {name}'s phone_country_code must be a number! Found: '{country_code}'")

print("--- SCHEMA VALIDATION COMPLETE ---")