import pandas as pd
import matplotlib.pyplot as plt

def plot_sentiment_pie_chart():
    try:
        # Load the data
        df = pd.read_excel('Oppenheimer_Stemmed_Tokens.xlsx')
        
        # Count sentiments
        sentiment_counts = df['label'].value_counts()
        
        if len(sentiment_counts) == 0:
            print("No sentiment data found")
            return

        # Set up pie chart
        plt.figure(figsize=(10, 8))
        
        # Create pie chart
        colors = ['#66b3ff', '#ff9999']  # Blue for positive, Red for negative
        explode = (0.05, 0)  # Slightly explode the first slice
        wedges, texts, autotexts = plt.pie(
            sentiment_counts,
            labels=sentiment_counts.index,
            autopct='%1.1f%%',
            startangle=90,
            colors=colors,
            explode=explode,
            textprops={'fontsize': 14}
        )

        # Customize autopct text color
        for autotext in autotexts:
            autotext.set_color('white')
            autotext.set_weight('bold')

        # Equal aspect ratio ensures pie is drawn as a circle
        plt.axis('equal')  
        plt.title('Sentiment Distribution in Oppenheimer Reviews', 
                 fontsize=16, pad=20, weight='bold')
        
        # Add legend
        plt.legend(
            wedges,
            sentiment_counts.index,
            title="Sentiments",
            loc="center left",
            bbox_to_anchor=(1, 0.5)
        )
        
        # Add subtitle with count information
        plt.text(
            -1.5, -1.3, 
            f"Total Reviews: {sum(sentiment_counts)}\n" +
            f"Positive: {sentiment_counts.get('positive', 0)}\n" +
            f"Negative: {sentiment_counts.get('negative', 0)}", 
            fontsize=12,
            bbox=dict(facecolor='white', alpha=0.7)
        )
        
        plt.tight_layout()
        plt.show()

    except Exception as e:
        print(f"Error creating pie chart: {str(e)}")

# Run the function
plot_sentiment_pie_chart()
