import tweepy
import time
from datetime import datetime
import os
from dotenv import load_dotenv
from dateutil.relativedelta import relativedelta
from telegram import Bot
from telegram.error import TelegramError

load_dotenv()

# Twitter API credentials
consumer_key = os.getenv("CONSUMER_KEY")
consumer_secret = os.getenv("CONSUMER_SECRET")
access_token = os.getenv("ACCESS_TOKEN")
access_token_secret = os.getenv("ACCESS_TOKEN_SECRET")

# Telegram API credentials
telegram_api_key = os.getenv("TELEGRAM_API_KEY")
telegram_chat_id = os.getenv("TELEGRAM_CHAT_ID")

# Initialize the Telegram bot
telegram_bot = Bot(token=telegram_api_key)

# Twitter API authentication
auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)
api = tweepy.API(auth)

# It will be updated every 60 seconds to avoid Twitter API rate limit.
INTERVAL = 60

# Earthquake time
earthquake_time = datetime(2023, 2, 6, 4, 17, 0)


# Calculate the time since the earthquake and update the profile bio.
def update_bio():
    now = datetime.now()
    time_since_earthquake = relativedelta(now, earthquake_time)

    years, months, days = time_since_earthquake.years, time_since_earthquake.months, time_since_earthquake.days
    hours, minutes = time_since_earthquake.hours, time_since_earthquake.minutes

    new_bio = f"Mechatronic Engineer | Senior Software Developer | Kahramanmaraş depremi üzerinden "

    if years > 0:
        new_bio += f"{years} yıl "
    if months > 0:
        new_bio += f"{months} ay "
    if days > 0:
        new_bio += f"{days} gün "

    new_bio += f"{hours} saat {minutes} dakika geçti. Otomatik olarak güncellenmektedir."

    # print(len(new_bio)) # Description should be less than 160 characters.

    try:
        api.update_profile(description=new_bio)
        print(f"Profile bio has been updated: {new_bio}")
        # telegram_bot.send_message(chat_id=telegram_chat_id, text=f"Profile bio has been updated: {new_bio}")
        # Tested to see if Telegram API works.
    except tweepy.TweepError as e:
        print(f"Profile update error: {e}")
        try:
            telegram_bot.send_message(chat_id=telegram_chat_id, text=f"Profile update error: {e}")
        except TelegramError as te:
            print(f"Telegram error: {te}")


while True:
    update_bio()
    time.sleep(INTERVAL)
