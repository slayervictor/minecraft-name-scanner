import requests
from bs4 import BeautifulSoup
import time

def IsUsernameTaken(username: str):
    if len(username) <= 15:
        time.sleep(0.25)
        url = f"https://laby.net/@{username}"
        headers = {
            "User-Agent": "Mozilla/5.0"
        }

        response = requests.get(url, headers=headers)
        response.raise_for_status()

        soup = BeautifulSoup(response.text, "html.parser")

        profile_name = soup.find("h1")
        if profile_name is None:
            return False
        else:
            return True
    else:
        return True