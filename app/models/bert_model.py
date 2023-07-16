from sentence_transformers import SentenceTransformer

def create_bert_model(model_name='all-MiniLM-L6-v2'):
    model = SentenceTransformer(model_name)
    return model
