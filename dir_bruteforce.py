import requests

target = input("Enter target URL: ")

directories = [
    "admin",
    "login",
    "dashboard",
    "uploads",
    "api",
    "test",
    "config"
]

print("\n[+] Starting Directory Bruteforce...\n")

for directory in directories:
    url = f"{target}/{directory}"

    try:
        response = requests.get(url, timeout=3)

        if response.status_code == 200:
            print(f"[FOUND] {url}")

        elif response.status_code == 403:
            print(f"[FORBIDDEN] {url}")

        else:
            print(f"[NOT FOUND] {url}")

    except requests.exceptions.RequestException:
        print(f"[ERROR] {url}")
