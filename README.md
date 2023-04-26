# Dynamic Twitter Bio Updater

## Inspiration

Unfortunately, a major earthquake occurred in Kahramanmaraş, Turkey on February 6, 2023, at 04:17 AM local time, with a magnitude of 7.7, which served as a harsh reminder of the country's vulnerability to such disasters. Just nine hours later, a second earthquake with a magnitude of 7.6 took place approximately 100 kilometers north of the first one. The two powerful earthquakes caused widespread destruction, impacting 11 cities and resulting in numerous damaged and collapsed buildings, as well as increased fatalities and injuries.

People tend to forget quickly, and in light of these tragic events, I wanted to help raise awareness about the disaster and remind people of its consequences. To do this, I decided to create a Python script that updates my Twitter bio every minute with the time elapsed since the first earthquake, using my native language, Turkish.

## Requirements

* Python 3.6+
* tweepy library 
* python-dotenv library 
* python-telegram-bot library 
* Twitter Developer account and API keys 
* Telegram bot and API key

## Installation

### Create a Virtual Environment

First, download the project and go to the main folder of the project.

Create a virtual environment using the following command:

Windows:

```bash
python -m venv venv
venv\Scripts\activate
```

Mac/Linux:

```bash
python3 -m venv venv
source venv/bin/activate
```

## Setting up the .env File
Copy the env-example file to create your own .env file:

```bash
cp env-example .env
```

Then, open the `.env` file and replace the `YOUR_CONSUMER_KEY`, `YOUR_CONSUMER_SECRET`, `YOUR_ACCESS_TOKEN` and `YOUR_ACCESS_TOKEN_SECRET` placeholders with your actual Twitter API keys and tokens. For Telegram notification, it is up to you.

## Installing Dependencies
After activating the virtual environment, install the packages from the `requirements.txt` file:

```bash
pip install -r requirements.txt
```

## Usage

While the virtual environment is active, run the script:

```bash
python twitter_bio_updater.py
```

This Python script utilizes the Twitter API and Telegram API to update a user's Twitter profile bio to highlight the time elapsed since a specific event (in this case, the Kahramanmaraş earthquake). Here's a summary of how the script works:

 1. Imports necessary libraries and initializes environment variables for Twitter and Telegram API credentials. 
 2. Sets up the Twitter API authentication and initializes the Telegram bot. 
 3. Defines an interval of 60 seconds to avoid hitting Twitter API rate limits. 
 4. Sets the earthquake's date and time as a datetime object.
 5. Defines a function `update_bio()` that calculates the time elapsed since the earthquake and updates the user's Twitter bio accordingly. The function takes into account the years, months, days, hours, and minutes passed since the event and composes the new bio text.
 6. Within the `update_bio()` function, it attempts to update the user's profile description (bio) with the new text using the Twitter API. If successful, it prints the updated bio to the console. In case of any errors, it prints the error message and sends it via the Telegram bot to the specified chat ID.
 7. The script then runs the `update_bio()` function in an infinite loop with a 60-second interval between iterations.

## Screenshot

![My Twitter Profile](images/my-twitter-profile.png)

## License

[MIT License](LICENSE)
