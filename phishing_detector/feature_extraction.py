from sklearn.feature_extraction.text import TfidfVectorizer
import pickle

def create_vectorizer(texts):

    """
    Create and fits a TF-IDF Vectorizer on the provided texts
    Saves the vectorizer to a file
    """

    vectorizer = TfidfVectorizer(max_features=3000) # Use top 3000 frequent words
    vectorizer.fit(texts)

    with open('models/tfidf_vectorizer.pkl', 'wb') as f:
        pickle.dump(vectorizer, f)
    
    print("TF-IDF Vectorizer created and saved")
    return vectorizer

def transform_text(texts, vectorizer_path='models/tfidf_vectorizer.pkl'):
    """
    Loads a saved vectorizer and transforms new text data.
    """
    with open(vectorizer_path, 'rb') as f:
        vectorizer = pickle.load(f)

    return vectorizer.transform(texts)