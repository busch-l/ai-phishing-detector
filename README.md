# AI-Powered Phishing Email Detector

A machine learning application built in Python to classify emails as malicious (phishing) or legitimate. This project uses natural language processing (NLP) techniques and a classic machine learning model to analyze email text and predict its intent.

## Project Status

**⚠️ In Development:** The core architecture, machine learning pipeline, and interactive command-line interface are complete. The primary task remaining is to source and integrate a high-quality public dataset for training and evaluation. The current code expects a CSV file but does not include one.

## Features

-   **Text Preprocessing:** Cleans raw email text by removing punctuation, converting to lowercase, removing common English stop words, and applying stemming.
-   **TF-IDF Feature Extraction:** Converts cleaned text into a meaningful numerical representation using `TfidfVectorizer`.
-   **Logistic Regression Model:** A simple yet effective classification model to distinguish between phishing and legitimate emails.
-   **Interactive CLI:** A user-friendly command-line interface to input new email text and receive a real-time prediction with an associated confidence score.
-   **Modular Codebase:** The project is structured into logical components for data processing, feature extraction, model training, and prediction.

## How It Works: The ML Pipeline

The project follows a standard machine learning pipeline for text classification:

1.  **Data Preprocessing (`data_preprocessing.py`):** Raw email text is passed through a cleaning function that uses `re` and `nltk` to normalize the text, making it suitable for feature extraction.
2.  **Feature Extraction (`feature_extraction.py`):** The cleaned text is transformed into numerical vectors using the Term Frequency-Inverse Document Frequency (TF-IDF) technique. The `TfidfVectorizer` learns the vocabulary from the training data and is saved for later use.
3.  **Model Training (`model.py` & `train.py`):** A Logistic Regression model is trained on the TF-IDF vectors. The script evaluates the model's accuracy on a test set and saves the trained model and vectorizer to the `/models` directory using `pickle`.
4.  **Prediction (`predict.py` & `main.py`):** For new, unseen email text, the interactive interface loads the saved model and vectorizer. It applies the same cleaning and transformation steps to the new text and uses the model to generate a prediction (Phishing or Legitimate) and a confidence score.

## Project Structure
phishing-detector/
├── data/
│ └── (empty - add your emails.csv here)
├── models/
│ └── (empty - trained models will be saved here)
├── phishing_detector/
│ ├── init.py
│ ├── data_preprocessing.py
│ ├── feature_extraction.py
│ └── model.py
├── main.py # Runs the interactive CLI
├── predict.py # Logic for making single predictions
├── train.py # Main script to train the model
└── README.md

## Future Work

-   [ ] **Source a Dataset:** Find and integrate a robust, publicly available email dataset.
-   [ ] **Experiment with Models:** Test other classification algorithms like Naive Bayes, Support Vector Machines (SVM), or more advanced deep learning models like LSTMs.
-   [ ] **Hyperparameter Tuning:** Use techniques like GridSearchCV to find the optimal parameters for the model and vectorizer.
-   [ ] **Develop a Web Interface:** Create a simple web application using Flask or Streamlit to provide a more user-friendly interface.
