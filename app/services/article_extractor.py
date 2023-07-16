import requests
from bs4 import BeautifulSoup

class Article_Extractor:
    def __init__(self, url):
        self.url = url

    def get_text(self):
        # Make a request to the website
        r = requests.get(self.url)
        r.raise_for_status()

        # Parse the HTML content
        soup = BeautifulSoup(r.text, 'html.parser')

        # Extract the text from all paragraph ('p') tags
        text = ' '.join([p.text for p in soup.find_all('p')])

        return text
