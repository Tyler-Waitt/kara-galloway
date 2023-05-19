import requests
from bs4 import BeautifulSoup

def get_url_text(url):
    response = requests.get(url)

    if response.status_code == 200:
        soup = BeautifulSoup(response.content, 'html.parser')
        text = soup.get_text()
        return text
    else:
        print('Error:', response.status_code)
