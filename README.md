# News Article Recommender System

This repository contains the code for a News Article Recommender System, which fetches news articles based on a user-provided topic and recommends similar articles based on a chosen text. The recommender system uses either TF-IDF or BERT embeddings to generate vector representations of the articles, and cosine similarity to find the most similar articles, prioritizing for the most recent articles of the topic so that the user can be kept up to date on the topic of their choice. 

The main files in this repository are:

- `app.py`: The main script that prompts the user for a topic, fetches news articles based on that topic, and calls the `get_similar_articles` function.
- `get_similar_articles.py`: This script defines the `get_similar_articles` function, which calculates the cosine similarity between a provided article and all fetched articles, and returns the most similar ones.
- `models/bert_model.py`: This script defines a function to create a BERT embeddings model.

## Installation

1. Clone the repository: `git clone https://github.com/your_username/news_article_recommender.git`
2. Change your directory: `cd news_article_recommender`
3. Install the requirements using pip: `pip install -r requirements.txt`

## Usage

1. Run the `app.py` script: `python app.py`
2. Enter a topic when prompted. The script will then fetch news articles based on that topic.
3. The script will return the 10 most similar articles to the provided example article.

Please note that you need to replace `'your_news_api_key_here'` in `app.py` with your actual News API key.

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project is licensed under the terms of the MIT license.

## Acknowledgements

Thanks to News API for providing the news article data, and to the creators of the `transformers` and `sentence-transformers` libraries for their work on BERT embeddings.
