from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from models.bert_model import create_bert_model
import numpy as np

def get_similar_articles(input_article, articles, model_type='tfidf'):
    """
    Given an input article and a list of articles (each a dictionary containing 'content' and 'url'), 
    finds and returns the 10 most similar articles.
    """
    article_texts = [article['content'] for article in articles]

    if model_type == 'tfidf':
        vectorizer = TfidfVectorizer()
        article_matrix = vectorizer.fit_transform(article_texts)
        input_vector = vectorizer.transform([input_article])

    elif model_type == 'bert':
        model = create_bert_model()
        article_matrix = model.encode(article_texts, convert_to_tensor=True).numpy()
        input_vector = model.encode([input_article], convert_to_tensor=True).numpy()

    cosine_sim = cosine_similarity(input_vector, article_matrix).flatten()
    sim_scores = list(enumerate(cosine_sim))
    sim_scores = sorted(sim_scores, key=lambda x: x[1], reverse=True)
    sim_scores = sim_scores[1:11]
    article_indices = [i[0] for i in sim_scores]

    return [articles[i]['url'] for i in article_indices]
