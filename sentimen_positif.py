from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from ast import literal_eval

def load_data(file_path):
    """Load data from Excel file and extract positive sentiment text"""
    df = pd.read_excel(file_path)
    
    # Handle cases where tokens might be stored as strings
    if 'filtered_tokens' in df.columns:
        df['tokens'] = df['filtered_tokens'].apply(
            lambda x: literal_eval(x) if isinstance(x, str) else x
        )
    
    # Filter positive sentiment rows and combine tokens
    positive_text = df[df['label'] == 'positive']['tokens'].sum()
    return ' '.join(positive_text)

def generate_wordcloud(text, output_file='positive_wordcloud.png'):
    """Generate and save a word cloud"""
    wordcloud = WordCloud(
        width=1600,
        height=900,
        background_color='white',
        colormap='viridis',
        max_words=200,
        collocations=False,
        stopwords={'his', 'it', 'even'}
    ).generate(text)
    
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(output_file, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"Word cloud saved as {output_file}")

if __name__ == "__main__":
    # File paths (modify as needed)
    input_file = 'Oppenheimer_Stemmed_Tokens.xlsx'  # Your sentiment-analyzed data
    
    # Load and process data
    text_data = load_data(input_file)
    
    # Generate and display word cloud
    generate_wordcloud(text_data)
