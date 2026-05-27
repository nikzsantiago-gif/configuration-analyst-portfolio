## 📌 Project Overview
This project simulates an automated data ingestion gateway for high-volume client payloads. In a CPaaS ecosystem, structural anomalies in client data (like text strings input into numeric phone routing fields) can cause downstream database crashes or failed deliveries. This lightweight Python engine audits data types against strict schema rules before processing.

## 🛠️ Tech Stack & Skills Demonstrated
* **Languages & Formats:** Python, JSON
* **Core Concepts:** Data Type Constraints, Payload Inspection, Bulk Data Processing, Error Isolation

## ⚙️ How It Works
1. **`user_payload.json`**: Simulates incoming API transaction data from clients, containing user IDs, names, account metrics, and phone country codes.
2. **`schema_check.py`**: A programmatic validator that maps out each user profile object and applies structural logic tests (e.g., verifying that the phone country code contains strictly numerical values, not alphabet characters).

## 📊 Sample Outputs
When data payloads match the expected system types perfectly:
```text
--- STARTING DATABASE SCHEMA VALIDATION ---
✅ PASS: Alice Smith's profile layout is correct.
--- SCHEMA VALIDATION COMPLETE ---
```

When a data corruption or schema breach is identified (e.g., text found in a numeric field):
```text
--- STARTING DATABASE SCHEMA VALIDATION ---
❌ FAIL: Bob Jones's phone_country_code must be a number! Found: 'INVALID_CODE_TEXT'
--- SCHEMA VALIDATION COMPLETE ---
```
