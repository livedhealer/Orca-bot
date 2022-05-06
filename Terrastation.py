# Terrastation.py
from multiprocessing.connection import wait
from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import time

"""
Control flow:

----------init------------
[x] Click "Connect" button
[x] Click "Wallet Connect" button
[x] Wait for user to do the thing...
- Once user input complete, click drop downs and show all checkbox
----------after liquidation----------
- Enter amounts
- Swap bluna -> luna -> UST -> aUST
- Enter password
-------------Todo------------------
[x] create verifyElementContainsText() function to make sure we're clicking what we think we're clicking...
[x] catch NoSuchElement Exceptions every time we use a driver.find_ method... This'll let us gracefully handle website updates that move buttons around on us...
[x] instead of .implicitly_wait method calls, use loops or builtin functions that watch for something to populate...
"""



class TerraStation:

    def __init__(self):
        self.driver = webdriver.Chrome(".\chromedriver.exe")

        #User creds stored for plugging into website prompts when completing the swaps...
        self.username = ""
        self.password = ""
        self.terraStationURL = "https://station.terra.money/swap" 

        #Get the driver pointed towards the Terra Station swap webpage...
        self.driver.get(self.terraStationURL)
 
        # self.driver.implicitly_wait(7) #Identified as the method to get button to be clicked
        # connect = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/button")
        # connect.click()
        try:
            connect = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/div/header/div/div/button")))
            self.verifyElementContainsText(connect, "Connect")
            connect.click()
        except TimeoutException:
            print("Red alert! Either item does not exist or internet connection timed out.")
 
 
        try:
            walletConnect = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/section/div/section/button[2]")))
            self.verifyElementContainsText(walletConnect, "Wallet Connect")
            walletConnect.click()
        except TimeoutException:
            print("Red alert! Either item does not exist or internet connection timed out.")

        self.driver.implicitly_wait(1) #Identified as the method to get button to be clicked

        #Wait while the QR code popup is on screen... 
        popupOnScreen = True
        while popupOnScreen:
            try:
                popup = self.driver.find_element_by_class_name("wallet-wc-modal--content")
            except NoSuchElementException:
                popupOnScreen = False

        connect = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/button") #


#Make sure the webElement contains the text specified before proceeding. If not, kill the program. 
# In the future, it would be very nice to get a phone alert under these circumstances...
    def verifyElementContainsText(self, webElement, text):
        if(webElement.text.__contains__(text)):
            print(webElement.text + " contains " + text)
            return 
        else:
            print("Red alert! " + webElement.text + " does not contain " + text)
            exit()
            return
            

    def showAtrributes(self):
        print(self.terraStationURL,self.username, self.password)