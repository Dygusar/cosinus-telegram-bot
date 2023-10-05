import logging
from aiogram import Bot, Dispatcher, types
from aiogram.dispatcher.filters import Command
from aiogram.contrib.middlewares.logging import LoggingMiddleware
from os import getenv
from dotenv import load_dotenv


load_dotenv()

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from selenium.webdriver.common.by import By
# import time
# import asyncio
from aiogram import executor

# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.ui import WebDriverWait
# from selenium.webdriver.common.action_chains import ActionChains
# from selenium.webdriver.common.keys import Keys
# from PIL import Image

API_TOKEN = getenv("API_TOKEN")
LOGIN = getenv("LOGIN")
PASSWORD = getenv("PASSWORD")

logging.basicConfig(level=logging.INFO)

bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)
dp.middleware.setup(LoggingMiddleware())

Options = webdriver.ChromeOptions()
Options.add_argument('--headless')
Options.add_argument('--disable-blink-features=AutomationControlled')
Options.add_experimental_option('excludeSwitches', ['enable-logging'])
chrome_driver_path = 'chromedriver.exe'
Options.add_argument('--window-size=1100,950')
    
async def plan(message):
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=Options)
    driver.get("https://nticosinuswawa.mobidziennik.pl/dziennik/planlekcji?typ=podstawowy")
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(LOGIN)
    driver.find_element(By.XPATH, '//*[@id="haslo"]').send_keys(PASSWORD)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[3]/input').click()
    driver.get("https://nticosinuswawa.mobidziennik.pl/dziennik/planlekcji?typ=podstawowy")
    driver.execute_script("window.scrollBy(0, 250);")
    driver.save_screenshot('main.png')
    driver.close()
    with open("main.png", "rb") as file:
        await bot.send_photo(chat_id=message.chat.id, photo=file)

async def domashka(message):
    s = Service(chrome_driver_path)
    driver = webdriver.Chrome(service=s, options=Options)
    driver.get('https://nticosinuswawa.mobidziennik.pl/dziennik/kalendarzklasowy')
    driver.find_element(By.XPATH, '//*[@id="login"]').send_keys(LOGIN)
    driver.find_element(By.XPATH, '//*[@id="haslo"]').send_keys(PASSWORD)
    driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div[2]/form/div[3]/input').click()
    driver.get('https://nticosinuswawa.mobidziennik.pl/dziennik/kalendarzklasowy')
    driver.execute_script("window.scrollBy(0, 240);")
    driver.save_screenshot('main.png')
    driver.close()
    with open("main.png", "rb") as file:
        await bot.send_photo(chat_id=message.chat.id, photo=file)


async def help(message):
    await message.answer('план - росклад, план, розклад, plan, росписание або /rozklad')
    
dp.register_message_handler(plan, Command("rozklad"))
dp.register_message_handler(plan, lambda msg: msg.text.lower() in ["росклад", "план", "розклад", "plan", "росписание"])
dp.register_message_handler(domashka, lambda msg: msg.text.lower() in ["домашка"])

dp.register_message_handler(help, Command("help"))



if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)