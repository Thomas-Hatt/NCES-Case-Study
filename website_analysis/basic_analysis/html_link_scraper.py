# Import required libraries
import requests
import pandas as pd
import re
from bs4 import BeautifulSoup
from pprint import pprint
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow
import sys

# Defined here is an example of how I will combine the URL to find the individual webpages.
# I filter all the URLS that match '?s=MI' and also indclude '&id='    
# exampleurl = '?s=MI&zc=48503&zd=50&of=3&id=169983'
# print(base_url + exampleurl)

# Get data from the URL
base_url = "https://nces.ed.gov/collegenavigator/" # Includes no parameters selected

url = "https://nces.ed.gov/collegenavigator/?s=MI&zc=48503&zd=50&of=3" # Specifically targeting Universities within a 50 miles radius of 48503

# Make a connection to the website
data = requests.get(url).text

# Create an instance of BeautifulSoup
soup = BeautifulSoup(data, 'html.parser')

# Locate all tables with the "itables" class
tables = soup.find_all('table', class_='itables')

# Create a list to store all the URLs in
url_list = list()

# Create a list to store all the University Names in
university_name_list = list()

# Create a number to track the total amount of URLs
total_urls = 0

# Create a number to track the total amount of University names
total_university_names = 0

# Change the max width of the dataframe to ensure the information fits
pd.set_option('display.max_colwidth', 1000)

# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ #
# --------------------------------------------------------- #   
# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ # 

# -- Function to track the names of the Universities -- #

for name in soup.find_all("td", class_="pbe"):
    # Strip the text and separate each <td> with a comma
    name = (name.get_text(strip=True, separator=', '))

    # Delete all text after the first comma
    result = name.partition(',')[0]

    # Print the name of the University (optional)
    # print(result)
    
    # Add the base_url to the list
    university_name_list.append(result)

    # Increment the total amount of University names
    total_university_names += 1  

# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ #
# --------------------------------------------------------- #   
# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ # 

# -- Function to track all URLs -- #

# Check if the item contains all required characters
for a in soup.find_all('a', href=True):
    # Print all URLS found (optional)
    # print("Found the URL:", a['href'])
    
    # Check to see if the characters "id=" are contained in the URL
    if 'id=' in a['href']:
        # Print a statement (optional)
        # print(" -- Found a URL that has '&id=' -- ")
        
        # Add the base_url to the list
        url_list.append(base_url + a['href'])
        
        # Increment the total amount of URLs
        total_urls += 1
        
    elif ('id=' in a['href'] == 0):
        print('sad')
        break
  
# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ #
# --------------------------------------------------------- #   
# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ # 

# -- Dataframes Initialization and Functions -- #

df_lst_uni_name = pd.DataFrame(university_name_list)
df_lst_url = pd.DataFrame(url_list)

# Function to merge two dataframes together
def MergeTwoDataframes(dataframe1, dataframe2):
    # Merge the dataframes column-wise
    df_merged = pd.concat([df_lst_uni_name + ',', df_lst_url], axis=1)
    
    # Return the merged dataframe
    return df_merged

# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ #
# --------------------------------------------------------- #   
# __--__--__--__--__--__--__--__--__--__--__--__--__--__--_ # 
  
# Print out each list
print('URL List: ')
pprint(url_list)

print('University Name List: ')
pprint(university_name_list)

# Merge the two dataframes and print them
merged = MergeTwoDataframes(df_lst_uni_name, df_lst_url)
print ('Merged Dataframes: University Name List, URL List')
print(merged)

# Print the total amount of URLs found
print('Total URLs Found: ' + str(total_urls))

# Print the total amount of University names found
print('University Names Found: ' + str(total_university_names))