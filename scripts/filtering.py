import pandas as pd

def load_data(file_path):
    """Load the Excel file and return the DataFrame."""
    try:
        data = pd.read_excel(file_path)
        return data
    except Exception as e:
        print(f"Error loading data: {str(e)}")
        return None

def filter_words(tokens, min_length=3, stopwords=None, unwanted_words=None):
    """Filter words based on length and specified criteria."""
    if stopwords is None:
        stopwords = set()
    if unwanted_words is None:
        unwanted_words = set()

    # Filter tokens
    filtered_tokens = [
        word for word in tokens
        if len(word) >= min_length and word.lower() not in stopwords and word.lower() not in unwanted_words
    ]
    return filtered_tokens

def process_reviews(data):
    """Process the reviews to filter words."""
    # Assuming the DataFrame has a 'text' column with tokenized text
    if 'text' not in data.columns:
        print("No 'text' column found in the data.")
        return

    # Load stopwords and unwanted words
    stopwords = {'the', 'is', 'in', 'and', 'to', 'a', 'of', 'it', 'that', 'this', 'for', 'but', 'he', 'she', 'they'}
    unwanted_words = {'movie', 'film', 'one', 'will', 'even'}

    # Process each review
    def safe_tokenize(x):
        """Convert text to a list of words, handling different formats."""
        if isinstance(x, str):
            # Split the string into words
            return x.split()  # Split by whitespace
        return []

    # Apply tokenization and filtering
    data['filtered_tokens'] = data['text'].apply(lambda x: filter_words(safe_tokenize(x), stopwords=stopwords, unwanted_words=unwanted_words))

    return data

def main():
    # Load the data
    file_path = 'Oppenheimer_label_tokenized.xlsx'
    data = load_data(file_path)

    if data is not None:
        # Process the reviews to filter words
        processed_data = process_reviews(data)

        # Display the first few rows of the processed data
        print("Processed Data with Filtered Tokens:")
        print(processed_data[['text', 'filtered_tokens']].head())

        # Optionally, save the processed data to a new Excel file
        output_file_path = 'Oppenheimer_Filtered_Tokens.xlsx'
        processed_data.to_excel(output_file_path, index=False)
        print(f"Processed data saved to {output_file_path}")

if __name__ == "__main__":
    main()
