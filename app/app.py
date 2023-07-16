import requests
import pandas as pd
import json
from services.get_similar_articles import get_similar_articles
from services.article_extractor import Article_Extractor
from models.topic_generator import Topic_Generator 

class KeyManager:
    def get_api_key(self, keyName):
        file = open("keys/currentKeys.json", "r")
        d = json.load(file)
        return d[keyName]

def get_news_data(api_key, topic):
    # Base URL for getting news articles
    url = 'https://newsapi.org/v2/everything'
    # Parameters for the API request
    parameters = {
        'q': topic,
        'language': 'en',
        'apiKey': api_key
    }

    # Send the API request
    response = requests.get(url, params=parameters)

    # If the request was successful, return the articles data
    if response.status_code == 200:
        articles = response.json()['articles']

        # Extract 'content' and 'url' from each article
        data = [{'content': article['content'], 'url': article['url']} for article in articles]

        return data
    else:
        print(f'Error: {response.status_code}')
        return None

def main():
    # Your News API key
    key = KeyManager()
    api_key = key.get_api_key("NewsKey")

    # Ask the user for a topic
    topic = input('Enter a topic: ')

    # Get the articles data
    article_texts = get_news_data(api_key, topic)

    if article_texts is not None:
        input_link = input('Enter a hyperlink for an article: ')
        extractor = Article_Extractor(input_link)
        input_article = extractor.get_text()
        print(get_similar_articles(input_article, article_texts, 'bert'))

if __name__ == "__main__":
    main()
