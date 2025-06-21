# DVWA Brute Force Login Script

A Python script for performing dictionary-based brute force attacks on DVWA (Damn Vulnerable Web Application) login.

## Features

- Sends HTTP POST requests to DVWA login form  
- Uses user-supplied password list  
- Detects successful login by checking response content  
- Gracefully handles request errors and missing files  

## Requirements

- Python 3 installed on your system  
- `requests` library  

Install `requests` if not already installed:

```bash
pip install requests
```

## Usage

1. Make sure DVWA is running and accessible (e.g., via XAMPP or Docker).  
2. Run the script:

```bash
python dvwa_bruteforce.py
```

3. Enter the path to your password list file when prompted.

## Example Output

```
Enter password list location: passwords.txt
Tried: 12345
Tried: admin123
Password found => password
```

## Disclaimer

This script is for educational purposes only. Do not use it on systems without proper authorization.
