# PortSwigger Labs Automation Suite 🚀

Welcome to my central repository for automated vulnerability exploitation frameworks. This repository is dedicated to housing custom scripts, tools, and exploit chains engineered to solve advanced labs within the **PortSwigger Web Security Academy**.

The goal of this project is to moving past manual interception (Burp Suite Repeater/Intruder) and focusing on full programmatic exploitation using clean, structured development patterns.

---

## 📂 Repository Structure

The suite is organized systematically by vulnerability classifications:

### 🔹 [SQL Injection](./SQL-Injection)
A production-grade collection of injection automation frameworks covering:
* **Conditional Responses:** Boolean-driven dynamic extraction algorithms.
* **Conditional Errors:** Forcing backend database exception handlers (Oracle `1/0` crashes) to leak clean assets via HTTP 500 signals.
* **Time-Based Delays:** Asynchronous processing latency validation mechanisms using fine-tuned extraction thresholds.
* **Oracle Out-of-Band (OOB) Simulation Engine:** A custom multi-threaded Flask infrastructure prototype mimicking XML entity retrieval pipelines seamlessly.

---

## 🛠️ Tech Stack & Dependencies

* **Language:** Python 3.x, Bash
* **Core Libraries:** `requests`, `threading`, `flask`, `time`, `re`, `string`

---

## ⚙️ How to Use These Frameworks

1. Clone the master repository structure:
   ```bash
   git clone [https://github.com/rbrizwan89-ctrl/PortSwigger-Labs-Automation.git](https://github.com/rbrizwan89-ctrl/PortSwigger-Labs-Automation.git)
   cd PortSwigger-Labs-Automation
