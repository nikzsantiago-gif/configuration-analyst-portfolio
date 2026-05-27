# Project 3: Multi-Environment Drift Auditor

## 📌 Project Overview
This project targets environment reliability and configuration consistency across complex enterprise deployment pipelines. In platform systems, configuration states often 'drift' out of sync when features are activated in a Testing/Staging environment but overlooked for Production. This utility automates cross-environment comparisons to guarantee setting parity.

## 🛠️ Tech Stack & Skills Demonstrated
* **Languages & Formats:** Python, JSON
* **Core Concepts:** Environment Alignment, Feature-Flag Mapping, Risk Assessment, Configuration Drift Analysis

## ⚙️ How It Works
1. **`config_staging.json`**: Represents the cutting-edge testing state containing new features (e.g., rich media integrations, security encryption tags).
2. **`config_production.json`**: Represents the live public server environment state.
3. **`drift_auditor.py`**: A change-management script that opens both states simultaneously, runs an intersection mapping loop across their active variables, and instantly isolates which configuration keys were missing in the release pipeline.

## 📊 Sample Outputs
When environments are perfectly aligned and keys match across systems:
```text
--- RUNNING ENVIRONMENT DRIFT AUDIT ---
✅ Match: 'api_version' configuration is aligned across environments.
✅ Match: 'enable_whatsapp_rich_media' configuration is aligned across environments.
--- DRIFT AUDIT COMPLETE ---
```
When a release management omission occurs (e.g., a feature key is missing in production):
```text
--- RUNNING ENVIRONMENT DRIFT AUDIT ---
✅ Match: 'api_version' configuration is aligned across environments.
🚨 CONFIGURATION DRIFT DETECTED: Feature 'encryption_enabled' is active in Staging but MISSING in Production!
--- DRIFT AUDIT COMPLETE ---
```
