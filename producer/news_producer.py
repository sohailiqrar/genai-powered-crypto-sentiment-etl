import requests
import json
import time
import os
from dotenv import load_dotenv
from schema import clean_news_data


def get_crypto_news():
    print("Fetching crypto news from CryptoPanic...")

    load_dotenv()

    
    CRYPTOPANIC_TOKEN = os.getenv('CRYPTOPANIC_TOKEN')
    url = f"https://cryptopanic.com/api/developer/v2/posts/?auth_token={CRYPTOPANIC_TOKEN}"

    MAX_RETRIES = 3
    BACKOFF_SECONDS = 5

    for attempt in range(MAX_RETRIES):
        try:
            response = requests.get(url)
            response.raise_for_status() # Check if the request was successful

            if response.status_code == 429 or response.status_code == 503: # Rate limit or service unavailable
                time.sleep(BACKOFF_SECONDS)
                continue
        
            data = response.json()
            raw_news = data.get('results', [])
            
            cleaned_news = clean_news_data(raw_news)

            return cleaned_news

        except Exception as e:
            print(f"Error fetching data: {e}")
            return []

if __name__ == "__main__":
    news = get_crypto_news()

    # Print the first item clearly to verify
    if news:
        print(news)
        print(f"\nSuccess! Fetched {len(news)} articles.")
    else:
        print("No news found.")

