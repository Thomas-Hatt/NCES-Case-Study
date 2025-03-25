# Import required libraries
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup

# Get data from the URL
default_url = "https://nces.ed.gov/collegenavigator/" # Includes no parameters selected

url = "https://nces.ed.gov/collegenavigator/?s=MI&zc=48503&zd=50&of=3" # Specifically targeting Universities within a 50 miles radius of 48503

# Make a connection to the website
data = requests.get(url).text

# Create an instance of BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# Locate all tables with the "itables" class
tables = soup.find_all('table', class_='itables')

# Find and print all information in each table (University)
for table in tables:
  tr_tags = table.find_all('tr')

  for tr in tr_tags:

    td_tags = tr.find_all('td')

    for td in td_tags:
      text = td.get_text(strip=True, separator=', ')
      print(text)

    print('---------')