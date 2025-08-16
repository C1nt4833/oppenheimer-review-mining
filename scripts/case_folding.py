import pandas as pd

# Load the Excel file
data = pd.read_excel('Oppenheimer_label.xlsx')

# Display the first few rows of the dataframe to understand its structure
print("Original Data:")
print(data.head())

# Function to perform case folding
def case_folding(text):
    if isinstance(text, str):  # Check if the input is a string
        return text.lower()  # Convert to lowercase
    return text  # Return the original value if not a string

# Apply case folding to all string columns in the dataframe
for column in data.select_dtypes(include=['object']).columns:
    data[column] = data[column].apply(case_folding)

# Display the modified dataframe
print("Data After Case Folding:")
print(data.head())

# Optionally, save the modified dataframe to a new Excel file
output_file_path = 'Oppenheimer_label_case_folded.xlsx'
data.to_excel(output_file_path, index=False)
print(f"Case folded data saved to {output_file_path}")
