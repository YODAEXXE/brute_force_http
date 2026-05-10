# 🔥 brute_http

<p align="center">
  <img src="https://readme-typing-svg.demolab.com?font=Fira+Code&pause=1000&color=FF3C3C&center=true&vCenter=true&width=435&lines=Simple+HTTP+Brute+Force+Tool;Made+for+Private+Labs;Python+Automation+Project" />
</p>

<p align="center">
  ⚡ Simple HTTP POST brute force tool written in Python for educational purposes and private lab environments.
</p>

---

# 📌 Features

✅ HTTP POST brute force  
✅ Custom login parameters  
✅ Wordlist support  
✅ Colored terminal interface  
✅ Linux & Windows compatible  
✅ Lightweight and simple  

---

# ⚙️ Requirements

- Python 3
- requests

Install dependencies:

```bash
pip install requests

🚀 Usage
python brute_http.py <url> <username> <wordlist> <user_parameter> <password_parameter>
🧪 Example
python brute_http.py http://127.0.0.1/login admin rockyou.txt Login Password
📥 Arguments
Argument	Description
url	Target login form URL
username	Target username
wordlist	Path to password list
user_parameter	Username parameter name
password_parameter	Password parameter name
🌐 Example HTML Form
<input name="Login">
<input name="Password">

Example:

Login Password
⚡ How It Works
📂 Open wordlist
   ↓
🔁 Read passwords
   ↓
📡 Send HTTP POST requests
   ↓
🔍 Analyze response
   ↓
✅ Detect successful login
🧠 Request Structure
dados = {
    user_parameter: username,
    password_parameter: password
}
🖥️ Example Output
attempt 123456
attempt admin123
attempt qwerty

password found
############
shadow123
⚠️ Notes

The tool currently detects successful authentication by searching for:

"logout"

inside the HTTP response.

Some systems may use:

CSRF tokens
Session cookies
Redirects
Rate limiting
Custom responses

You may need additional modifications depending on the lab environment.

📚 Educational Purpose

This project was created for:

Python practice
HTTP automation learning
Cybersecurity studies
Private lab testing
❌ Disclaimer

This tool is intended strictly for authorized environments and educational purposes.

Do not use it against systems without explicit permission.

👨‍💻 Author
by fckmott
