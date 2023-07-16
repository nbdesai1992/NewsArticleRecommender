# This can be used to fine tune training for specific topics. Useful if the user 
# wants to fine tune topics and recommendatiosn for a particular repeated topic 
# or use case. 

from gensim import corpora
from gensim.models import LdaModel
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
from nltk.stem import WordNetLemmatizer
import string

class Topic_Generator:
    def __init__(self, num_topics=10, num_words=5):
        self.num_topics = num_topics
        self.num_words = num_words
        self.lda_model = None
        self.dictionary = None
        self.stop_words = set(stopwords.words('english'))
        self.lemmatizer = WordNetLemmatizer()

    def preprocess(self, text):
        # Tokenize, remove punctuation, lowercase, remove stopwords, and lemmatize
        tokens = word_tokenize(text)
        table = str.maketrans('', '', string.punctuation)
        tokens = [w.translate(table) for w in tokens]
        tokens = [w.lower() for w in tokens]
        tokens = [w for w in tokens if not w in self.stop_words]
        tokens = [self.lemmatizer.lemmatize(w) for w in tokens]
        return tokens

    def train(self, documents):
        # Preprocess the documents
        texts = [self.preprocess(doc) for doc in documents]

        # Create a dictionary representation of the documents
        self.dictionary = corpora.Dictionary(texts)

        # Create a bag-of-words representation of the documents
        corpus = [self.dictionary.doc2bow(text) for text in texts]

        # Train the LDA model
        self.lda_model = LdaModel(corpus, num_topics=self.num_topics, id2word=self.dictionary)

    def get_topics(self, text):
        # Preprocess the text
        tokens = self.preprocess(text)

        # Convert the tokens to bag-of-words format
        bow = self.dictionary.doc2bow(tokens)

        # Get the topic distribution of the text
        topic_distribution = self.lda_model.get_document_topics(bow)

        # Sort the topics by their probabilities, and get the top ones
        sorted_topics = sorted(topic_distribution, key=lambda x: x[1], reverse=True)

        # Extract the top topics and their words
        topics = []
        for topic_num, prob in sorted_topics[:self.num_words]:
            words = self.lda_model.show_topic(topic_num, topn=self.num_words)
            topic_words = [word for word, _ in words]
            topics.append((topic_num, prob, topic_words))

        return topics

