# Terrastation.py
from doctest import OutputChecker
from multiprocessing.connection import wait
from operator import truediv
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException

import time

"""
Control flow:

----------init------------
[x] Prompt user to input their TStation Password and finish setup of TStation extension

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
        self.lunaIntermediateAmount = ""
        self.chromeExtensionPage = "https://chrome.google.com/webstore/detail/terra-station/aiifbnbfobpmeekipheeijimdpnlpgpp"
        self.terraStationExtensionURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/swap" 

        #Get the driver pointed towards the Terra Station swap webpage...
        self.driver.get(self.chromeExtensionPage)

        try:
            addToChromeButton = WebDriverWait(self.driver, 10).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div[2]/div/div/div[2]/div[2]/div")))
            self.verifyElementContainsText(addToChromeButton, "Add to Chrome")
            addToChromeButton.click()
        except TimeoutException:
            print("Either addToChromeButton does not exist or internet connection timed out.")

        self.driver.implicitly_wait(1) #Identified as the method to get button to be clicked

        #TODO: Wait until popup is onscreen, then click the add extension button
        # popupOnScreen = False
        # while popupOnScreen:
        #     try:
        #         popup = self.driver.find_element_by_class_name("")
        #         popupOnScreen = True
        #         popup.click()
        #     except NoSuchElementException:
        #         popupOnScreen = False

        self.password = input("Enter your Terra Station password into the terminal to let me know that you've added the Terra Station Extension and logged in to your wallet...")

        self.driver.get(self.terraStationExtensionURL)

        self.driver.implicitly_wait(7)


    def swap(self, fromCoin, amount, toCoin):

        # Make sure we're already on the swap page of the Terra Station Extension
        if self.driver.current_url != self.terraStationExtensionURL:
            self.driver.get(self.terraStationExtensionURL)
            self.driver.implicitly_wait(7)

        # Click the dropdown arrows to expose the search bars and coin options
        fromDropDownButton = self.driver.find_element_by_xpath("/html/body/div[1]/article/div/section/article/section/form/div[1]/div/div/div/button")
        fromDropDownButton.click()
        toDropDownButton = self.driver.find_element_by_xpath ("/html/body/div[1]/article/div/section/article/section/form/div[3]/div/div/div/button")
        toDropDownButton.click()
        
        # Search bars are now exposed
        fromSearchBar = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[1]/div/div/section/div[1]/input")
        toSearchBar = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[3]/div/div/section/div[1]/input")

        # click on search windows and search for fromCoin and toCoin
        searches = ActionChains(self.driver)
        
        #search for fromCoin
        searches.click(on_element = fromSearchBar)
        searches.send_keys(fromCoin)

        #search for toCoin
        searches.click(on_element = toSearchBar)
        searches.send_keys(toCoin)

        #make it happen
        searches.perform()

        #Find and click the exposed elements representing the coins we want to swap
        toCoinElement = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[1]/div/div/section/div[2]/section/button")
        toCoinElement.click()

        fromCoinElement = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[3]/div/div/section/div[2]/section/button")
        fromCoinElement.click()

        #Click on amount window and input how much of the fromCoin we want to swap
        inputAmount = ActionChains(self.driver)

        #How much are we talkin about here...

        fromCoinAmountWindow = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[1]/div/div/div/input")
        inputAmount.click(on_element = fromCoinAmountWindow)
        inputAmount.send_keys(amount)
        inputAmount.perform()

        if fromCoin == "bLuna":
            self.extractTradeLunaAmount()

        enterPassword = ActionChains(self.driver)
        #Enter the password "/html/body/div/article/div/section/article/section/form/div[5]/div/div/input"
        passwordWindow = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[6]/div/div/input")
        enterPassword.click(on_element = passwordWindow)

        enterPassword.send_keys(self.password)

        submitButton = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[6]/button")
        enterPassword.click(on_element = submitButton)

        #Make that $$$
        enterPassword.perform()

        print("WE DID IT MR. OBAMA, WE SOLVED RACISM!!!")

        try:
            confirmButton = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/footer/button")))
            self.verifyElementContainsText(confirmButton, "Confirm")
            confirmButton.click()
        except TimeoutException:
            print("RED ALERT!!! Either confirmButton does not exist or transaction was never verified!!!.")


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

    def extractTradeLunaAmount(self):
        lunaValue = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[3]/div/div/div/span")
        while lunaValue.text.__contains__("Simulating"):
            lunaValue = self.driver.find_element_by_xpath("/html/body/div/article/div/section/article/section/form/div[3]/div/div/div/span")
        self.lunaIntermediateAmount = lunaValue.text[2:]

        print(self.lunaIntermediateAmount + " " + lunaValue.text)

    def showAtrributes(self):
        print(self.terraStationURL,self.username, self.password)