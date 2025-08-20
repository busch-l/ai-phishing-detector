from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score
import pickle

def train_and_evaluate_model(X_train, y_train, X_test, y_test):
    """
    Trains a Logistic Regression model, evaluates it, and returns it.
    """
    print("Training the Logistic Regression model...")
    model = LogisticRegression(max_iter=1000) # Added max_iter for convergence
    model.fit(X_train, y_train)
    
    # Evaluate the model
    y_pred = model.predict(X_test)
    accuracy = accuracy_score(y_test, y_pred)
    print(f"Model Accuracy: {accuracy:.4f}")
    
    return model

def save_model(model, path="models/phishing_detector_model.pkl"):
    """
    Saves the trained model to the specified path.
    """
    with open(path, 'wb') as f:
        pickle.dump(model, f)
    print(f"Model saved to {path}")