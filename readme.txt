# brute_http

Simple HTTP brute force tool written in Python for educational purposes and private lab testing.

## Features

* HTTP POST brute force
* Custom form parameter support
* Wordlist support
* Colored terminal interface
* Linux and Windows compatible

---

# Requirements

* Python 3
* requests library

Install requests with:

```bash id="79os6f"
pip install requests
```

---

# Usage

```bash id="b26yx0"
python brute_http.py <url> <username> <wordlist> <user_parameter> <password_parameter>
```

---

# Example

```bash id="k8lx0n"
python brute_http.py http://127.0.0.1/login admin rockyou.txt Login Password
```

---

# Arguments

| Argument           | Description                   |
| ------------------ | ----------------------------- |
| url                | Login form URL                |
| username           | Target username               |
| wordlist           | Path to the wordlist          |
| user_parameter     | Username field parameter name |
| password_parameter | Password field parameter name |

---

# Example HTML Form

```html id="nm6p7w"
<input name="Login">
<input name="Password">
```

In this case:

```bash id="y2f8cq"
Login Password
```

will be used as the request parameters.

---

# How It Works

The tool:

1. Opens the wordlist
2. Reads each password line by line
3. Sends an HTTP POST request
4. Analyzes the server response
5. Checks if `"logout"` exists in the response
6. If found, the password is considered valid

---

# POST Structure

```python id="h4c9vt"
dados = {
    user_parameter: username,
    password_parameter: password
}
```

---

# Example Output

```bash id="6l4e0r"
attempt 123456
attempt admin123
attempt qwerty

password found
############
shadow123
```

---

# Notes

* The script currently detects successful authentication by searching for the string `"logout"` in the HTTP response.
* Some systems may use:

  * redirects
  * CSRF tokens
  * session cookies
  * custom responses
  * rate limiting

Additional modifications may be required depending on the lab environment.

---

# Disclaimer

This tool was created strictly for:

* educational purposes
* automation practice
* authorized testing
* private laboratory environments

Do not use it against systems without explicit authorization.

---

# Author

by fckmott
