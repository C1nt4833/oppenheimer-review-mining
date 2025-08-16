import pandas as pd
import joblib
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.naive_bayes import MultinomialNB
from sklearn.metrics import classification_report, accuracy_score, confusion_matrix, ConfusionMatrixDisplay
import matplotlib.pyplot as plt

def load_data(file_path):
    """Load data from Excel file."""
    try:
        return pd.read_excel(file_path)
    except Exception as e:
        print(f"Error loading {file_path}: {str(e)}")
        return None

def preprocess_data(data):
    """Preprocess the data to extract features and labels."""
    if 'text' not in data.columns or 'label' not in data.columns:
        raise ValueError("Data must contain 'text' and 'label' columns")
    
    X = data['text']
    y = data['label']
    return X, y

def train_model(X_train, y_train):
    """Train a Naive Bayes model using TF-IDF features."""
    vectorizer = TfidfVectorizer()
    X_train_tfidf = vectorizer.fit_transform(X_train)
    
    model = MultinomialNB()
    model.fit(X_train_tfidf, y_train)
    
    return model, vectorizer

def evaluate_model(model, vectorizer, X_test, y_test):
    """Evaluate the model on the test data."""
    X_test_tfidf = vectorizer.transform(X_test)
    y_pred = model.predict(X_test_tfidf)
    
    print("\nClassification Report:")
    print(classification_report(y_test, y_pred))
    print("Accuracy:", accuracy_score(y_test, y_pred))
    
    # Plot confusion matrix
    cm = confusion_matrix(y_test, y_pred)
    disp = ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=model.classes_)
    disp.plot(cmap='Blues')
    plt.title('Confusion Matrix')
    plt.show()

def main():
    # Load training data
    training_data_path = 'tfidf_data_latih.xlsx'  # Your training data file
    training_data = load_data(training_data_path)
    
    if training_data is None:
        return
    
    # Preprocess training data
    X_train, y_train = preprocess_data(training_data)
    
    # Train the model
    print("Training the model...")
    model, vectorizer = train_model(X_train, y_train)
    
    # Load test data
    test_data_path = 'tfidf_data_uji.xlsx'  # Your test data file
    test_data = load_data(test_data_path)
    
    if test_data is None:
        return
    
    # Preprocess test data
    X_test, y_test = preprocess_data(test_data)
    
    # Evaluate the model
    print("Evaluating the model...")
    evaluate_model(model, vectorizer, X_test, y_test)

if __name__ == "__main__":
    main()
