import pandas as pd
from wordcloud import WordCloud
import matplotlib.pyplot as plt
from ast import literal_eval
from collections import Counter

def display_combined_word_cloud(text, title="Oppenheimer Reviews Word Cloud"):
    """Generate and display a word cloud from combined text"""
    if not text or len(text.split()) < 5:
        print("Not enough words to display word cloud")
        return
    
    # Create and configure word cloud
    wc = WordCloud(
        width=1200,
        height=800,
        background_color='white',
        colormap='plasma',
        max_words=200,
        collocations=False,  # Don't count word pairs
        stopwords={'his', 'with', 'was', 'will', 'even', 'the','are','you'}
    ).generate(text)
    
    # Display settings
    plt.figure(figsize=(16, 10))
    plt.imshow(wc, interpolation='bilinear')
    plt.title(title, fontsize=24, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.show()

# Load the data
try:
    df = pd.read_excel('Oppenheimer_Stemmed_Tokens.xlsx')
    
    # Find text column with fallbacks
    text_col = next((col for col in ['tokens', 'text'] 
                    if col in df.columns), None)
    
    if not text_col:
        print("No text column found in the data")
    else:
        # Safely convert strings to lists
        def safe_to_list(x):
            try:
                if isinstance(x, str):
                    return literal_eval(x) if x.startswith('[') else x.split()
                return []
            except:
                return []
        
        df['tokens'] = df[text_col].apply(safe_to_list)
        
        # Get all words and their frequencies
        all_words = [word for sublist in df['tokens'] for word in sublist]
        word_counts = Counter(all_words)
        
        print(f"\nFound {len(word_counts)} unique words in {len(all_words)} total words")
        print("Top 100 words:", word_counts.most_common(100))
        
        # Combine all text for word cloud
        combined_text = ' '.join(all_words)
        display_combined_word_cloud(combined_text)

except Exception as e:
    print(f"Error processing data: {str(e)}")
