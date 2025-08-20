import pickle
from phishing_detector.data_preprocessing import clean_text
from phishing_detector.feature_extraction import transform_text

def predict_email(email_text): 
    """
    Predicts if an email is phishing or not.
    """
    #1. Load the saved model and vectorizer
    try: 
        with open('models/phishing_detector_model.pkl', 'rb') as f:
            model = pickle.load(f)
    except FileNotFoundError:
        return "Error: Model not found. Please run train.py first"
    
    #2 Clean and transform input text
    cleaned_text = clean_text(email_text)
    text_vector = transform_text([cleaned_text])

    #3. Make prediction
    prediction = model.predict(text_vector)
    probability = model.predict_proba(text_vector)

    #4. Return result
    if prediction[0] == 1:
        return f"Prediction: Phishing (Confidence: {probability[0][1]:.2%})"
    else:
        return f"Prediction: Legitimate (Confidence: {probability[0][0]:.2%})"

if __name__ == '__main__':
    # Example usage
    new_email = "Subject: Urgent account verification required! Click http://totally-not-a-scam.com/login to secure your account."
    result = predict_email(new_email)
    print(result)

    another_email = "Hey, just wanted to check in about our meeting tomorrow at 3 PM. Let me know if that still works. Thanks"
    result = predict_email(another_email)
    print(result)