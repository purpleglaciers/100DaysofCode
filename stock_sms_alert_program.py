import requests
import datetime
from twilio.rest import Client

STOCK = "TSLA"
COMPANY_NAME = "Tesla Inc"

STOCK_ENDPOINT = "https://www.alphavantage.co/query"
NEWS_ENDPOINT = "https://newsapi.org/v2/everything"

NEWS_API_KEY = "YOUR_NEWSAPI.ORG_KEY"
ALPHAVANTAGE_API_KEY = "YOUR_ALPHAVANTAGE_API_KEY"

account_sid = "YOUR_TWILIO_ACCOUNT_SID"
auth_token = "YOUR_TWILIO_AUTH_TOKEN"

today = datetime.date.today()
yesterday = today - datetime.timedelta(days=1)
dby = today - datetime.timedelta(days=2)

get_news = False

# TODO 1: Get closing positions for chosen stock from yesterday and day before yesterday (dby)
stock_price_response = requests.get(f"https://www.alphavantage.co/query?"
                                    f"function=TIME_SERIES_DAILY_ADJUSTED&symbol={STOCK}&"
                                    f"outputsize=compact&apikey={ALPHAVANTAGE_API_KEY}")
stock_info = stock_price_response.json()
close_dby = float(stock_info['Time Series (Daily)'][f'{str(dby)}']['4. close'])
close_y = float(stock_info['Time Series (Daily)'][f'{str(yesterday)}']['4. close'])

# TODO 2: Calculate change in positions by getting the positive difference (pos_dif) check if 5% change
five_perc_close_y = close_y / 20
pos_dif = 0

if close_dby >= close_y:
    pos_dif = (close_dby - close_y)
    gain_loss_indicator = "🔻"
    perc_change = round((pos_dif / close_dby) * 100)
else:
    pos_dif = (close_y - close_dby)
    gain_loss_indicator = "🔺"
    perc_change = round((pos_dif / close_y) * 100)

# TODO 3: If STOCK price increase/decreases by 5% between yesterday and the day before yesterday print("Get News").
if pos_dif >= five_perc_close_y:
    get_news = True

print(f"close_dby = {close_dby}\nclose_y = {close_y}")

# TODO 4: Get the first 3 articles for the COMPANY_NAME.
news_api_response = requests.get(f"https://newsapi.org/v2/everything?q={COMPANY_NAME}&apiKey={NEWS_API_KEY}")

news_data = news_api_response.json()
first_3_articles = news_data["articles"][:3]

# TODO 5: Send alerts if stock price fluctuated >= 5%
client = Client(account_sid, auth_token)

for article in first_3_articles:
    message = client.messages.create(
        to="YOUR_#",
        from_="YOUR_TWILIO_FROM_#",
        body=f"{STOCK}: {gain_loss_indicator}%{perc_change}"
             f"\nHeadline: {article['title']}"
             f"\nBrief: {article['description']}")
