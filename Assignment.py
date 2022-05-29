import time
import requests
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from bs4 import BeautifulSoup

class assignment():
    url = "https://www.zenclass.in/login"
    data = requests.get(url)
    soup = BeautifulSoup(data.content, 'lxml')
    driver = webdriver.Firefox()

    def my_login(self,username,password):
        #function to login into the website
        u_name=username
        pwd=password
        self.driver.get(self.url)
        element=self.driver.find_element(by=By.XPATH, \
            value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[1]/div/input')
        element.send_keys(u_name)
        element=self.driver.find_element(by=By.XPATH, \
            value='/html/body/div/div/div/div[1]/div[2]/div/div[1]/form/div[2]/div/input')
        element.send_keys(pwd)
        element.send_keys(Keys.RETURN)

    def displayall_data(self):
        #function to display left panel data
        self.my_login('truptidesai09@gmail.com','Trupti#09')
        time.sleep(5)
        data=self.driver.find_element(by=By.XPATH, \
            value='/html/body/div/div[2]/div/div[1]/div/div[1]/div[1]')
        with open("datafile.txt","w") as f:
            f.write(data.text)
            f.close()

    def add_queries(self):
        #function to add new queries
        #self.my_login('truptidesai09@gmail.com','Trupti#09')
        time.sleep(5)
        query_link = self.driver.find_element(by=By.XPATH, \
            value='/html/body/div/div[1]/nav/ul/div[6]/li/span/div/div[2]')
        query_link.click()
        qry = self.driver.find_element(by=By.XPATH, \
            value='/html/body/div/div[2]/div/div[2]/div[1]/div[1]')
        qry.click()
        for i in range(0,5):
            newquery_button = self.driver.find_element(by=By.XPATH, \
                value= '/html/body/div/div[2]/div/div[1]/div[1]/button')
            newquery_button.click()
            cancel_btn = self.driver.find_element(by=By.XPATH, value=\
                '/html/body/div/div[2]/div/div[2]/div[6]/div[2]/div/div/section[3]/div[2]/button[1]')
            cancel_btn.click()
            time.sleep(5)
            category = Select(self.driver.find_element(by=By.XPATH, \
                value= '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[1]/select'))
            category.select_by_index(1)
            subcategory = Select(self.driver.find_element(by=By.XPATH, \
                value= '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[2]/select'))
            subcategory.select_by_index(3)
            language = Select(self.driver.find_element(by=By.XPATH, \
                value= '/html/body/div/div[2]/div/div[2]/div/div/form/div[2]/div[4]/select'))
            language.select_by_index(1)
            time.sleep(5)
            title = self.driver.find_element(by=By.XPATH, \
                value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/div/input')
            title.send_keys("Guvi Python AT 1 &2 Automation Project")
            description= self.driver.find_element(by=By.XPATH, \
                value='/html/body/div/div[2]/div/div[2]/div/div/form/div[5]/textarea')
            description.send_keys("This is a Project Test Code Running for the \
                Python Automation 1&2 Project Given by mentor Mr. Suman Gangopadhyay.")
            create_btn = self.driver.find_element(by=By.XPATH, \
                value='/html/body/div/div[2]/div/div[2]/div/div/form/div[13]/div/button')
            create_btn.click()
            time.sleep(5)

a = assignment()
a.displayall_data()
a.add_queries()
