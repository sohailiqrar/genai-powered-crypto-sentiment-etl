import json
from dotenv import load_dotenv
from GenAI.gemini import get_gemini_response
from data.sample_data import get_sample_news_data, get_sample_gemini_response, get_sample_price_data
from producer.crypto_news import get_crypto_news
from producer.crypto_price import get_crypto_price
from producer.schema import clean_news_data
from producer.eventhub_client import send_to_eventhub
from azure.eventhub import EventData
import json
import os

load_dotenv()

if __name__ == "__main__":
    crypto_api_data = get_crypto_news()
    # crypto_api_data = get_sample_news_data()

    # print("Raw Crypto News Data:")
    # print(json.dumps(crypto_api_data, indent=2))

    news_data = get_gemini_response(crypto_api_data)

    # news_data = get_sample_gemini_response()
    # print("Gemini Response:")
    # print(json.dumps(news_data, indent=2))

    price_data = get_crypto_price()

    # price_data = get_sample_price_data()
    # print("Crypto Price Data:")
    # print(json.dumps(price_data, indent=2))

    send_to_eventhub(
        eventhub_con=os.getenv("EVENTHUB_CONNECTION_STRING"),
        eventhub_name=os.getenv("NEWS_EVENTHUB_NAME"),
        event_envelopes=news_data
    )

    send_to_eventhub(
        eventhub_con=os.getenv("EVENTHUB_CONNECTION_STRING"),
        eventhub_name=os.getenv("PRICE_EVENTHUB_NAME"),
        event_envelopes=price_data
    )

    # event_envelopes = {"news_data": json.dumps(news_data), "price_data":json.dumps(price_data)}

    # print("Prepared event envelopes:")
    # print(json.dumps(event_envelopes, indent=2))

    # producer = get_eventhub_producer()
    # batch = producer.create_batch()

    # for event in event_envelopes:
    #     event_data = EventData(json.dumps(event))
    #     try:
    #         batch.add(event_data)
    #     except ValueError:
    #         producer.send_batch(batch)
    #         batch = producer.create_batch()
    #         batch.add(event_data)

    # if len(batch) > 0:
    #     producer.send_batch(batch)

    # producer.close()

    # # Print the first item clearly to verify
    # if event_envelopes:
    #     print(f"\nSuccess! Fetched {len(event_envelopes)} articles.")
    # else:
    #     print("No news found.")




    