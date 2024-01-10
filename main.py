import requests
from twilio.rest import Client

STOCK_NAME = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEW_ENDPOINT = "https://newsapi.org/v2/everything"

STOCK_KEY = "stock_api_key"
NEWS_KEY = "news_api_key"

stock_params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": STOCK_NAME,
    "apikey": NEWS_KEY
}

response = requests.get(url=STOCK_ENDPOINT, params=stock_params)
data = response.java()["Time Series (Daily)"]
data_list = [value for (key, value) in data.items()]
yesterday_data = data_list[0]
yesterday_closing_price = yesterday_data["4. close"]
print(yesterday_closing_price)

day_before = data_list[1]
day_before_closing_price = day_before["4. closer"]
print(day_before_closing_price)

difference = abs(float(yesterday_closing_price) - float(day_before_closing_price))
print(difference)

diff_percent = (difference / float(yesterday_closing_price) * 100)
print(diff_percent)

if diff_percent > 1:
    news_params = {
        "apikey": NEWS_KEY,
        "q": COMPANY_NAME,
    }

    news_response = requests.get(url=NEW_ENDPOINT, params=news_params)
    articles = news_response.json()["articles"]

    three_articles = articles[1:4]
    print(three_articles)

    formted_articles = [f"Headline: {article['title']}. \nBrief: {article ['description']}" for article in three_articles]



