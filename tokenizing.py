import pandas as pd
import nltk
from nltk.tokenize import word_tokenize

# Ensure necessary NLTK resources are downloaded
nltk.download('punkt', quiet=True)

# Load the Excel file
file_path = 'Oppenheimer_label_case_folded.xlsx'
data = pd.read_excel(file_path)

# Display the first few rows of the dataframe to understand its structure
print("Original Data:")
print(data.head())

# Function to tokenize text with error handling
def tokenize_text(text):
    try:
        if isinstance(text, str):
            return word_tokenize(text)
        return text  # Return original value if not string
    except Exception as e:
        print(f"Error tokenizing text: {e}")
        return text  # Return original value on error

# Apply tokenization to all string columns in the dataframe
for column in data.select_dtypes(include=['object']).columns:
    data[column] = data[column].apply(tokenize_text)

# Display the tokenized data
print("Data After Tokenizing:")
print(data.head())

# Optionally save the tokenized data to a new Excel file
output_file_path = 'Oppenheimer_label_tokenized.xlsx'
data.to_excel(output_file_path, index=False)
print(f"Tokenized data saved to {output_file_path}")
