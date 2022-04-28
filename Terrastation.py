# Terrastation.py
from multiprocessing.connection import wait
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
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
[] create verifyElementContainsText() function to make sure we're clicking what we think we're clicking...
[] catch NoSuchElement Exceptions every time we use a driver.find_ method... This'll let us gracefully handle website updates that don't ask us for permission first.
"""



class TerraStation:

    def __init__(self):
        self.driver = webdriver.Chrome(".\chromedriver.exe")

        #Get the driver pointed towards the Terra Station swap webpage...
        self.terraStationURL = "https://station.terra.money/swap" 
        self.driver.get(self.terraStationURL)
 
        self.driver.implicitly_wait(5) #Identified as the method to get button to be clicked
 
        connect = self.driver.find_element_by_xpath("/html/body/div[1]/div/header/div/div/button")
        connect.click()
 
        self.driver.implicitly_wait(1) #Identified as the method to get button to be clicked
 
        walletConnect = self.driver.find_element_by_xpath("/html/body/div[4]/div/div/section/div/section/button[2]")
        walletConnect.click()

        self.driver.implicitly_wait(1) #Identified as the method to get button to be clicked

        #Wait while the QR code popup is on screen... 
        popUpOnScreen = True
        while popUpOnScreen:
            try:
                self.driver.find_element_by_class_name("wallet-wc-modal--content")
            except NoSuchElementException:
                print("Successfully waited for user to connect")
                popUpOnScreen = False

        #User creds stored for plugging into website prompts when completing the swaps...
        self.username = ""
        self.password = ""


    def showAtrributes(self):
        print(self.terraStationURL,self.username, self.password)