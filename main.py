import requests
from bs4 import BeautifulSoup
import sqlite3
from datetime import datetime

url = "https://meteofor.com.ua/weather-ternopil-4951/"
response = requests.get(url)
soup = BeautifulSoup(response.text, 'html.parser')

temperature_element = soup.find(class_='temperature')
temperature = temperature_element.text.strip()

current_datetime = datetime.now().strftime('%Y-%m-%d %H:%M:%S')

conn = sqlite3.connect('weather_database.db')
cursor = conn.cursor()

cursor.execute('''
    CREATE TABLE IF NOT EXISTS weather_data (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        datetime TEXT NOT NULL,
        temperature TEXT NOT NULL
    )
''')
