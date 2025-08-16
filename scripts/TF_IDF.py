import pandas as pd
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
import pickle

def load_data(file_path):
    """Load and preprocess data from Excel file"""
    try:
        df = pd.read_excel(file_path)
        print("Data loaded successfully. Sample:")
        print(df.head())
        return df
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def preprocess_text(text_series):
    """Basic text preprocessing (customize as needed)"""
    return text_series.str.lower().str.replace('[^\w\s]', '')

def tfidf_weighting(data, text_column='text', max_features=5000):
    """Perform TF-IDF vectorization and return weighted features"""
    # Initialize vectorizer with common parameters
    vectorizer = TfidfVectorizer(
        max_features=max_features,
        stop_words='english',
        ngram_range=(1, 2),  # Include unigrams and bigrams
        min_df=5,            # Ignore terms appearing in <5 docs
        max_df=0.7           # Ignore terms appearing in >70% docs
    )
    
    print("\nFitting TF-IDF vectorizer...")
    X = vectorizer.fit_transform(data[text_column])
    
    # Get feature names and their IDF weights
    feature_names = vectorizer.get_feature_names_out()
    idf_values = vectorizer.idf_
    
    # Create DataFrame of TF-IDF features
    tfidf_df = pd.DataFrame(
        X.toarray(), 
        columns=feature_names
    )
    
    return tfidf_df, vectorizer

def main():
    # Configuration
    DATA_FILE = 'data_uji.xlsx'  # Your input file
    TEXT_COLUMN = 'text'          # Column containing text data
    SAVE_VECTORIZER = True        # Save vectorizer for later use
    
    # Load and prepare data
    data = load_data(DATA_FILE)
    if data is None:
        return
    
    print("\nPreprocessing text...")
    data['clean_text'] = preprocess_text(data[TEXT_COLUMN])
    
    # Perform TF-IDF transformation
    tfidf_features, vectorizer = tfidf_weighting(
        data, 
        text_column='clean_text',
        max_features=5000
    )
    
    # Combine with original data
    final_data = pd.concat([data, tfidf_features], axis=1)
    
    # Save results
    output_file = 'tfidf_data_uji.xlsx'
    final_data.to_excel(output_file, index=False)
    
    
    print("\nProcess completed successfully!")

    # Show most important terms by average TF-IDF weight
    print("\nTop terms by average TF-IDF weight:")
    print(tfidf_features.mean().sort_values(ascending=False).head(20))

if __name__ == "__main__":
    main()
