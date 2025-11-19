import requests
from bs4 import BeautifulSoup

def IsUsernameTaken(username: str):
    """
    Scrape the Laby.net profile page for the given username.
    Returns:
        - dict of profile data if the account exists
        - False if the account does NOT exist
    """
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