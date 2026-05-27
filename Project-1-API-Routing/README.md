# CPaaS API Routing & Configuration Validator

## 📌 Project Overview
An automated, localized testing environment built to simulate how Configuration Analysts manage and audit routing logic within a cloud communications platform (CPaaS). This tool ensures system properties conform to enterprise business rules, preventing configuration drift and message delivery failures before deployment.

## 🛠️ Tech Stack & Skills Demonstrated
* **Languages & Formats:** Python, JSON
* **Core Concepts:** Configuration Management, Data Validation, Automated System Auditing, Exception Handling, Risk Mitigation

## ⚙️ How It Works
The system consists of two primary components:
1. **`routing_config.json`**: Acts as the environment's single source of truth, defining mock active API endpoints, communication channels (SMS/WhatsApp), and maximum retry limits.
2. **`validator.py`**: A lightweight logic engine that reads the active configurations and tests them against strict operational boundaries (e.g., ensuring message retry settings are safely above 0 to protect service availability).

## 📊 Sample Outputs
When the configuration rules are met safely:
```text
--- STARTING CONFIGURATION AUDIT ---
Checking environment: Production
✅ SUCCESS: 'sms_max_retries' configuration is valid and safe.
--- AUDIT COMPLETE ---
```

When an unsafe boundary condition is found (e.g., retries set to 0):
```text
--- STARTING CONFIGURATION AUDIT ---
Checking environment: Production
❌ ERROR: 'sms_max_retries' cannot be 0. System will fail to resend dropped messages.
--- AUDIT COMPLETE ---
```
