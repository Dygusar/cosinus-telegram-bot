# cosinus-telegram-bot

This project is a Telegram bot specifically designed to help students manage their diaries and coursework through the convenience of Telegram. The bot offers a range of features to simplify the daily tasks and responsibilities of students, allowing them to access their academic information on the go.

## Getting Started

1. Install all the necessary dependencies using requirements.txt:
pip install -r requirements.txt

2. After configuring your .env file with the correct values, start the bot:
python main.py

## Setup Instructions

Before you can start using this bot, you need to configure your `.env` file with the following environment variables:

1. `API_TOKEN` - This is the token for your bot, which you obtained from BotFather on Telegram.
2. `LOGIN` - This is the login for accessing your student account on Technikum Cosinus IT (if you plan to use such functionality).
3. `PASSWORD` - This is the password for accessing your student account on Technikum Cosinus IT (if you plan to use such functionality).

The environment variables in the `.env` file should look like this:

```env
API_TOKEN=your_token
LOGIN=your_login
PASSWORD=your_password
```
