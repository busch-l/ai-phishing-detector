import re
import nltk
from nltk.corpus import stopwords
from nltk.stem import PorterStemmer

def clean_text(text):
    """
    Cleans the input email text.
    -Removes Punctuation and Numbers
    -Converts to lowecase
    -Removes Stopwords
    -Stems words
    """
    # Remove non alphabetic characters and convert to lowercase
    text = re.sub('[^a-zA-Z]', ' ', text).lower()
    # tokenize the text
    words = text.split()
    # Remove stopwords
    stop_words = set(stopwords.words('english'))
    words = [w for w in words if not w in stop_words]
    # Stemming
    stemmer = PorterStemmer()
    words = [stemmer.stem(w) for w in words]
    return " ".join(words)
    
# Example usage (remove this later)
if __name__ == '__main__':
    sample_email = "Hello, CONGRATULATIONS you've won a $1,000,000 prize! Click here http://scam.com to claim."
    cleaned_email = clean_text(sample_email)
    print("Original:\n", sample_email)
    print("\nCleaned:\n", cleaned_email)