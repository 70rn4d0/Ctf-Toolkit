import requests
with open("wordlist.txt") as f:
    for word in f:
        url = f"http://target.com/{word.strip()}"
        r = requests.get(url)
        if r.status_code == 200:
            print(f"Found: {url}")
