import requests
from bs4 import BeautifulSoup
import pandas as pd
import time

class OppenheimerReviewScraper:
    def __init__(self):
        self.base_url = "https://www.imdb.com"
        self.headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36'
        }
        self.movie_id = "tt15398776"  # Oppenheimer's IMDb ID

    def scrape_reviews(self, review_count=100):
        """Scrape specified number of review texts"""
        reviews = []
        page = 0
        
        print(f"Scraping {review_count} Oppenheimer reviews...")
        
        while len(reviews) < review_count:
            url = f"{self.base_url}/title/{self.movie_id}/reviews?start={page*25}"
            
            try:
                response = requests.get(url, headers=self.headers, timeout=10)
                response.raise_for_status()
                soup = BeautifulSoup(response.content, 'html.parser')
                
                for review in soup.find_all('div', class_='review-container'):
                    if len(reviews) >= review_count:
                        break
                    
                    text_element = review.find('div', class_='text')
                    if text_element:
                        reviews.append({
                            'text': text_element.get_text(strip=True)
                        })
                
                page += 1
                time.sleep(1.5)  # Be gentle with IMDb's servers
                
                # Stop if no more pages
                if not soup.find('div', class_='load-more-data'):
                    print("Reached end of reviews")
                    break
                    
            except Exception as e:
                print(f"Error scraping page {page}: {e}")
                continue
        
        return reviews[:review_count]  # Ensure perfect count

    def save_to_excel(self, reviews):
        """Save reviews to Excel with one 'text' column"""
        df = pd.DataFrame(reviews)
        
        # Configure Excel output
        df.to_excel(
            'Oppenheimer_100_data.xlsx',
            index=False,
            sheet_name='Reviews',
            columns=['text'],
            header=['Film Review Text']
        )
        
        print(f"Successfully saved {len(df)} reviews to Oppenheimer_100_data.xlsx")

def main():
    scraper = OppenheimerReviewScraper()
    reviews = scraper.scrape_reviews(100)
    
    if reviews:
        scraper.save_to_excel(reviews)
        print("\nExample review texts (first 3):")
        for i, review in enumerate(reviews[:3], 1):
            print(f"\nReview {i}:\n{review['text']}\n{'-'*50}")
    else:
        print("No reviews were scraped.")

if __name__ == "__main__":
    main()
