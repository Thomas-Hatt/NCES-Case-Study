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


for name in soup.find_all("td", class_="pbe"):
  # Strip the text and separate each <td> with a comma
  name = (name.get_text(strip=True, separator=', '))
    
  # Delete all text after the first comma
  result = name.partition(',')[0]
  
  # Loop through the "ipeds hoverID" class to get the IPEDS IDs and OPE IDs
  for ids in soup.find_all("p", class_="ipeds hoverID"):
    id = ids.get_text(strip=True, separator=', ')
    
    # Full IPEDS ID
    ipeds_id = id.partition('|')[0]
    
    # Full OPE ID
    ope_id = id.partition('|')[2]
    
  print(result)
  print(ipeds_id)
  print(ope_id)
  

# Find the element containing the text for IPEDS and OPE
element = soup.find_next_sibling('p', class_='ipeds hoverID')