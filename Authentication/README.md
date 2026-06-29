# PortSwigger Authentication Lab Automation (Expert Level)

This repository contains a dedicated automation utility designed to streamline password formatting constraints encountered during vulnerability research labs, specifically targeting nested validation design flaws.

## Lab Focus
* **Vulnerability:** Broken Brute-Force Protection (Multiple Credentials Per Request)
* **Severity:** Expert
* **Core Logic:** The target application accepts authentication arrays via JSON payloads but fails to validate single-credential strict tracking per request. 

## Utility Purpose
When handling large candidate wordlists (e.g., 100+ items), manually structure-formatting them into a standard `["pass1", "pass2", "pass3"]` raw bracket format on a single line for injection proxy frames is heavily time-consuming. This script processes clean carriage-return arrays automatically.

## Usage Guide
1. Place your target candidate password list inside `passwords.txt` (one per line).
2. Execute the parser:
   ```bash
   python3 automation_tool.py
