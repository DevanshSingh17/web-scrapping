# -*- coding: utf-8 -*-
"""web scrapping_1.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1bNb3CMnfKKYt-EeGxZAtFIrYEDpMfPOf

#WEB SCRAPING

USING PANDAS AND REAL WEBSITE FOR SCRAPING
"""

from bs4 import BeautifulSoup
import requests

url='https://en.wikipedia.org/wiki/List_of_largest_companies_in_the_United_States_by_revenue'
page=requests.get(url)
page

soup=BeautifulSoup(page.text,'html')
soup

"""#here we said find all tables which means all the tables present in the website will appear"""

soup.find_all('table')

"""#we can even use indexing to get the table we want"""

soup.find_all('table')[1]

"""#the other way to pull this out is"""

soup.find('table',class_='wikitable sortable')

table=soup.find_all('table')[1]
print(table)

"""#taking only 'th' tags"""

word_title=table.find_all('th')

"""here now we will take the text present in the th tag  nd .strip to remove all the backslashes"""

word_table_title=[title.text.strip() for title in word_title]
print(word_table_title)

import pandas as pd

df=pd.DataFrame(columns=word_table_title)
df

"""#now let us add the data using td tags and rows using tr tags"""

column_data=table.find_all('tr')
print(column_data)

for row in column_data:
  row_data=(row.find_all('td'))
  individual_row_data=[data.text.strip() for data in row_data]
  print(individual_row_data)

"""we can see that now we need to implement this all in our dataset but first remove any empty set like the 1st one where there is no data ('above number 1')"""

for row in column_data[1:]:
  row_data=(row.find_all('td'))
  individual_row_data=[data.text.strip() for data in row_data]
  #print(individual_row_data)
  length=len(df)
  df.loc[length]=individual_row_data   # this means it will append the data accordingly

df

"""# the above is our resultant dataframe ready now to undergo data ANALYSTS /ANALYSIS /PREDICTION /CLEANING"""

df.to_csv(r"C:\Users\DEVANSH SINGH TOMAR\OneDrive\Documents\DATA ANALYSTS\WEB SCRAPING\dataset\companies.csv",index=False)

df.to_excel(r"C:\Users\DEVANSH SINGH TOMAR\OneDrive\Documents\DATA ANALYSTS\WEB SCRAPING\dataset\Company.xlsx")

"""#BEAUTIFUL SOUP + REQUESTS"""