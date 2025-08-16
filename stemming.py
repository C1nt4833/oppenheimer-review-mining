import pandas as pd
from nltk.stem import PorterStemmer
import nltk

# Download NLTK data if not already present
nltk.download('punkt')

def stem_tokens(token_lists):
    """Apply stemming to a list of tokens"""
    stemmer = PorterStemmer()
    stemmed_tokens = []
    for token_list in token_lists:
        if isinstance(token_list, list):
            stemmed_tokens.append([stemmer.stem(word) for word in token_list])
        else:
            stemmed_tokens.append([])
    return stemmed_tokens

def main():
    # Load the filtered tokens data
    input_file = 'Oppenheimer_Filtered_Tokens.xlsx'
    try:
        df = pd.read_excel(input_file)
        
        # Check if filtered_tokens column exists
        if 'filtered_tokens' not in df.columns:
            print("Error: 'filtered_tokens' column not found in the input file")
            return
        
        # Convert string representations of lists to actual lists
        df['tokens'] = df['filtered_tokens'].apply(
            lambda x: eval(x) if isinstance(x, str) and x.startswith('[') else []
        )
        
        # Apply stemming
        print("Applying stemming to tokens...")
        df['stemmed_tokens'] = stem_tokens(df['tokens'])
        
        # Save the results
        output_file = 'Oppenheimer_Stemmed_Tokens.xlsx'
        df.to_excel(output_file, index=False)
        print(f"Stemmed data saved to {output_file}")
        
        # Show sample results
        print("\nSample of original and stemmed tokens:")
        print(df[['filtered_tokens', 'stemmed_tokens']].head())
        
    except Exception as e:
        print(f"Error processing file: {str(e)}")

if __name__ == "__main__":
    main()
