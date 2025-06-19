import requests
import time

# Website to ping
url = input("Enter the website URL to keep online: ").strip()

while True:
    try:
        print(f"Pinging {url} at {time.ctime()}")
        response = requests.get(url)
        print("✅ Status:", response.status_code)
        time.sleep(30)  # Simulate stay
    except Exception as e:
        print("❌ Error:", e)
    
    time.sleep(90)  # Wait rest of 2 mins
