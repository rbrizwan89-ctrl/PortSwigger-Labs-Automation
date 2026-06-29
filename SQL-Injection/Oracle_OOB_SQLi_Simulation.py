import re
import subprocess
import urllib.parse
import threading # 🧠 Naya: Background processing ke liye
from flask import Flask, request, render_template_string, redirect, url_for, flash

app = Flask(__name__)
app.secret_key = "super_secret_session_key_for_flash_messages"

DB_USERNAME = "administrator"
DB_PASSWORD = "Admin#Secur3_OOB_99x"

def trigger_dns_lookup(domain):
    """Yeh function alag se background mein chalega, website ko slow nahi karega"""
    try:
        print(f"[🔥] [DNS OUTBOUND] Database triggering network call to: {domain}")
        subprocess.Popen(f"nslookup {domain}", shell=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
    except:
        pass

def process_oracle_xml_query(cookie_value):
    try:
        if "EXTRACTVALUE" in cookie_value and "xmltype" in cookie_value:
            print("\n[+] [Oracle Engine] Valid Oracle OOB XML payload detected!")
            
            url_match = re.search(r'SYSTEM\s+"http://([^"]+)"', cookie_value, re.IGNORECASE)
            if url_match:
                raw_url = url_match.group(1)
                
                simulated_url = raw_url
                if "SELECT password" in cookie_value or "YOUR-QUERY-HERE" in cookie_value:
                    simulated_url = re.sub(r"'\s*\|\|.*?\|\|\s*'", DB_PASSWORD, raw_url)
                    simulated_url = simulated_url.replace("||(SELECT password FROM users WHERE username='administrator')", DB_PASSWORD)
                    simulated_url = simulated_url.replace("(SELECT password FROM users WHERE username='administrator')", DB_PASSWORD)
                
                final_domain = simulated_url.split('/')[0]
                
                # 🚀 THREADING: Isko background mein phenk diya taaki Burp Suite hang na ho
                t = threading.Thread(target=trigger_dns_lookup, args=(final_domain,))
                t.start()
                
    except Exception as e:
        print(f"[-] [Oracle Engine Error] Query Crash: {str(e)}")

@app.route('/')
def index():
    tracking_cookie = request.cookies.get('TrackingId', '')
    if tracking_cookie:
        decoded_cookie = urllib.parse.unquote(tracking_cookie)
        process_oracle_xml_query(decoded_cookie)

    html = """
    <!DOCTYPE html>
    <html>
    <head><title>Enterprise Analytics Dashboard</title></head>
    <body style="font-family: sans-serif; text-align: center; padding-top: 50px; background-color: #f4f6f9;">
        <h2>📊 Enterprise Product Tracking Portal</h2>
        <p style="color: green;">● HTTP/1.1 200 OK (Asynchronous Engine Active)</p>
        <a href="/login" style="font-weight:bold;">🔑 Go to Login Page</a>
    </body>
    </html>
    """
    return render_template_string(html)

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        if request.form.get('username') == DB_USERNAME and request.form.get('password') == DB_PASSWORD:
            return redirect(url_for('dashboard'))
        flash("Invalid credentials!")
    return render_template_string("<h2>Login</h2><form method='POST'>User: <input type='text' name='username'><br>Pass: <input type='password' name='password'><br><button type='submit'>Login</button></form>")

@app.route('/dashboard')
def dashboard():
    return "<h1>🏆 FLAG: OOB_SQLI_EXTRACTION_SUCCESS_MASTERED</h1>"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)