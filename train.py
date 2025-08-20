import pandas as pd
from sklearn.model_selection import train_test_split

# Import tools from our toolbox
from phishing_detector.data_preprocessing import clean_text
from phishing_detector.feature_extraction import create_vectorizer
from phishing_detector.model import train_and_evaluate_model, save_model

def main_training_pipeline():
    """
    The main pipeline to train the phishing detector.
    """
    print("Starting model training process...")

    # 1. Load Data
    try:
        df = pd.read_csv('data/emails.csv')
        # This is a common step: ensure your label column is numerical (0s and 1s)
        # If your labels are "spam" and "ham", you need to convert them.
        # Example: df['label'] = df['label'].map({'ham': 0, 'spam': 1})
    except FileNotFoundError:
        print("Error: 'data/emails.csv' not found. Please add your dataset.")
        return # Stop execution if there's no data

    # 2. Preprocess Text
    print("Cleaning and preprocessing text...")
    df['cleaned_text'] = df['text'].apply(clean_text)

    # 3. Feature Extraction
    print("Creating TF-IDF features...")
    X = df['cleaned_text']
    y = df['label']
    vectorizer = create_vectorizer(X) # This also saves the vectorizer
    X_tfidf = vectorizer.transform(X)

    # 4. Split Data
    X_train, X_test, y_train, y_test = train_test_split(X_tfidf, y, test_size=0.2, random_state=42)

    # 5. Train and Evaluate Model (using our new tool)
    trained_model = train_and_evaluate_model(X_train, y_train, X_test, y_test)

    # 6. Save the final model (using our new tool)
    if trained_model:
        save_model(trained_model)
        print("Training complete!")

# This makes the script runnable
if __name__ == '__main__':
    main_training_pipeline()
    