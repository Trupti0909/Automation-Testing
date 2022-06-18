from asyncio.windows_events import NULL
from bs4 import BeautifulSoup
from numpy import True_, append
import requests
import csv
import pandas as pd

class Assignment():

    def open_website_url(website_url):  
        data = requests.get(website_url)
        soup = BeautifulSoup(data.content, 'lxml')
        return soup

    def amazon_laptopdetails():
        url= "https://www.amazon.in/s?k=laptop+i5+8+gb+ram+with+1tb+hdd&crid=DMFAZR7DOV3V&sprefix=lapt%2Caps%2C3352&ref=nb_sb_noss_2"
        webdata=Assignment.open_website_url(url)
        products = []
        prices = [] 
        for data in webdata.find_all('div', class_='sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right'):
            names = data.find('span', class_='a-size-medium a-color a-text-normal')
            price = data.find('span', class_='a-offscreen')
            products.append(names.text)
            prices.append(price.text)
        output_data={'Product':tuple(products[0:5]),'Price':tuple(prices[0:5])}
        df_al = pd.DataFrame(output_data, columns= ['Product', 'Price'])
        return(df_al)        

    def amazon_mobiledetails():
        url="https://www.amazon.in/s?k=mobile+4g+6gb+ram+128gb+storage&crid=2KD3RG6U1QOBP&sprefix=mobile+4g+6gb+ram+128gb+storage%2Caps%2C2175&ref=nb_sb_noss_1"
        webdata=Assignment.open_website_url(url)
        products = []
        prices = [] 
        for data in webdata.find_all('div', attrs={'class':'sg-col sg-col-4-of-12 sg-col-8-of-16 sg-col-12-of-20 s-list-col-right'}):
            names = data.find('span', attrs={'class':'a-size-medium a-color a-text-normal'})
            price = data.find('span', attrs={'class':'a-offscreen'})
            products.append(names.text)
            prices.append(price.text)
        output_data={'Product':tuple(products[0:5]),'Price':tuple(prices[0:5])}
        df_am = pd.DataFrame(output_data, columns= ['Product', 'Price'])
        return(df_am)        

    def flipkart_laptopdetails():
        url="https://www.flipkart.com/search?q=laptop%20i5%208%20gb%20ram%20with%201tb%20hdd&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        webdata=Assignment.open_website_url(url)
        products = []
        prices = [] 
        for data in webdata.find_all('div', class_='_3pLy-c row'):
            names = data.find('div', class_='_4rR01T')
            price = data.find('div', class_='_30jeq3 _1_WHN1')
            products.append(names.text)
            prices.append(price.text)
        output_data={'Product':tuple(products[0:5]),'Price':tuple(prices[0:5])}
        df_fl = pd.DataFrame(output_data, columns= ['Product', 'Price'])
        return(df_fl)        
        
    def flipkart_mobiledetails():
        url="https://www.flipkart.com/search?q=mobile%204g%206gb%20ram%20128gb%20storage&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off"
        webdata=Assignment.open_website_url(url)
        products = []
        prices = [] 
        for data in webdata.find_all('div', class_='_3pLy-c row'):
            names = data.find('div', class_='_4rR01T')
            price = data.find('div', class_='_30jeq3 _1_WHN1')
            products.append(names.text)
            prices.append(price.text)
        output_data={'Product':tuple(products[0:5]),'Price':tuple(prices[0:5])}
        df_fm = pd.DataFrame(output_data, columns= ['Product', 'Price'])
        return(df_fm)        

    
    def write_to_excel():
        df1=Assignment.flipkart_laptopdetails()
        df2=Assignment.amazon_laptopdetails()
        df3=Assignment.flipkart_mobiledetails()
        df4=Assignment.amazon_mobiledetails()
        laptop_frames=[df1,df2]
        mobile_frames=[df3,df4]
        laptop_df=pd.concat(laptop_frames)
        mobile_df=pd.concat(mobile_frames)
        sorted_df_laptop=laptop_df.sort_values(by=['Price'])
        sorted_df_mobile=mobile_df.sort_values(by=['Price'])
        (laptop_df).to_excel (r'C:\Users\hp\Desktop\python_myworks\laptop_pricelist.xlsx',header=True)
        (mobile_df).to_excel (r'C:\Users\hp\Desktop\python_myworks\mobile_pricelist.xlsx',header=True)
        print(sorted_df_laptop.iloc[0:3])
        print(sorted_df_mobile.iloc[0:3])
        
Assignment.write_to_excel()
