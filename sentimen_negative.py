from wordcloud import WordCloud
import matplotlib.pyplot as plt
import pandas as pd
from collections import Counter
from ast import literal_eval

# Configuration
NEGATIVE_WORDCLOUD_FILE = "negative_wordcloud.png"
DATA_FILE = "Oppenheimer_Stemmed_Tokens.xlsx"  # Modify to your file
STOPWORDS = {'movie', 'film', 'one', 'will', 'even', 'oppenheimer', 'like', 'with', 'are', 'you','was','nolan','time','best','amazing','good','its','his','masterpiece','very','not','it','have','has','most','more','the','had'}  # Words to exclude
MAX_WORDS = 1000  # Limit number of words in cloud
NUM_TOP_WORDS = 20  # Number of top words to print

def load_negative_words(data_file):
    """Extract negative sentiment words from data file"""
    df = pd.read_excel(data_file)
    
    # Handle cases where tokens might be stored as strings
    if 'filtered_tokens' in df.columns:
        df['tokens'] = df['filtered_tokens'].apply(
            lambda x: literal_eval(x) if isinstance(x, str) else x
        )
    
    # Filter negative sentiment rows and flatten tokens
    negative_words = []
    for tokens in df[df['label'] == 'negative']['tokens']:
        if isinstance(tokens, list):
            negative_words.extend(tokens)
    
    # Count word frequencies and filter short words
    word_counts = Counter(
        word.lower() for word in negative_words 
        if len(word) >= 3 and word.lower() not in STOPWORDS
    )
    
    print(f"\nTop {NUM_TOP_WORDS} Negative Words:")
    for word, count in word_counts.most_common(NUM_TOP_WORDS):
        print(f"{word}: {count} times")
    
    return ' '.join(negative_words)

def generate_negative_wordcloud(text):
    """Generate and save negative sentiment word cloud"""
    wordcloud = WordCloud(
        width=1600,
        height=900,
        background_color='white',
        colormap='Reds',  # Red color scheme for negative sentiment
        max_words=MAX_WORDS,
        collocations=False,
        stopwords=STOPWORDS
    ).generate(text)
    
    plt.figure(figsize=(20, 10))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.title("Negative Review Word Cloud", fontsize=24, pad=20)
    plt.axis('off')
    plt.tight_layout()
    plt.savefig(NEGATIVE_WORDCLOUD_FILE, dpi=300, bbox_inches='tight')
    plt.show()
    print(f"\nNegative sentiment word cloud saved as {NEGATIVE_WORDCLOUD_FILE}")

if __name__ == "__main__":
    print("Generating negative sentiment word cloud...")
    negative_text = load_negative_words(DATA_FILE)
    generate_negative_wordcloud(negative_text)
