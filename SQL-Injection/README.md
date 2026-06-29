# SQL Injection (SQLi) Automation Suite

This directory contains production-grade exploitation scripts designed to automate data extraction from various advanced SQL Injection vulnerabilities found within the PortSwigger Web Security Academy.

## 🛠️ Included Tools

### 1. 🎯 Blind SQLi BruteForcer (`Blind_SQLi_BruteForce.py`)
* **Vulnerability Type:** Blind SQLi (Conditional Responses)
* **Mechanics:** Analyzes HTML response signatures for string flags (e.g., `Welcome back!`) to dynamically determine database password length and brute-force the administrator hash character-by-character.

### 2. ⚡ Conditional Error Exfiltrator (`Conditional_Errors_SQLi_Automation.py`)
* **Vulnerability Type:** Blind SQLi (Conditional Errors / Error-Based)
* **Mechanics:** Targets backend relational engines (like Oracle) by injecting database-specific mathematical error blocks (e.g., `TO_CHAR(1/0)` via `CASE WHEN` conditions) to force HTTP 500 status responses when character extraction tests ring true.

### 3. ⏱️ Time-Based Blind Extractor (`Time_Based_SQLi_Automation.py`)
* **Vulnerability Type:** Blind SQLi (Time-Based Delays)
* **Mechanics:** Injects sub-queries leveraging time-sleep hooks (e.g., `pg_sleep(5)`). Measures asynchronous latency metrics (`time.time()`) to extract clean data assets when response validation tags exceed a 4.5-second processing threshold.

### 4. 🧬 Oracle Out-of-Band (OOB) Simulator (`Oracle_OOB_SQLi_Simulation.py`)
* **Vulnerability Type:** Out-of-Band (OOB) SQLi Simulation Engine
* **Mechanics:** A custom Flask mock platform designed to test XML/External Entity style data exfiltration via `EXTRACTVALUE`. Features multi-threaded background parsing and asynchronous shell execution (`nslookup`) to handle continuous inbound network calls safely without locking up testing threads.
