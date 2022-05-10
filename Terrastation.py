# Terrastation.py
from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.chrome.options import Options 
import time


class TerraStation:

    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.password = ""
        self.lunaIntermediateAmount = ""
        self.terraStationExtensionSwapURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/swap"
        self.terraStationExtensionLoginURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/auth/recover"


        addPluginOption = self.addTerraStationPlugin()
        # Kickstart the webdriver and add the Terra Station plugin
        self.driver = webdriver.Chrome(".\chromedriver.exe", options=addPluginOption) #Use Chrome...
        self.driver.get(self.terraStationExtensionLoginURL)
        self.addTerraStationPlugin()
        self.initializeWallet()

        #User creds stored for plugging into website prompts when completing the swaps...

        self.driver.implicitly_wait(7)


    def swap(self, fromCoin, amount, toCoin):

        # Make sure we're already on the swap page of the Terra Station Extension
        if self.driver.current_url != self.terraStationExtensionSwapURL:
            self.driver.get(self.terraStationExtensionSwapURL)

        self.refresh() # make sure we have up-to-date values in the wallet... CRITICAL. Aaaarrrg!

        try:
            fromDropDownButton = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/article/div/section/article/section/form/div[1]/div/div/div/button")))
            fromDropDownButton.click()
        except TimeoutException:
            print("RED ALERT!!! Could not locate fromDropDownButton button, so swap could not be processed")       

        # Click the dropdown arrows to expose the search bars and coin options
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
            confirmButton = WebDriverWait(self.driver, 600).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[4]/div/div/footer/button")))
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

    def addTerraStationPlugin(self):
        options = webdriver.ChromeOptions()
        options.add_extension("./Terra2.9.0_0.crx")
        return options

    def initializeWallet(self):

        # Read and save user credentials from file
        loginInfo = ["", "", ""]
        i = 0
        with open(self.fileLocation) as file:
            for line in file:
                loginInfo[i] = line
                i+=1
        file.close()
        self.password = loginInfo[1] #Save for transaction confirmations!!

        # Wait until the form is loaded, then input user credentials, and finally click submit
        formEntry = ActionChains(self.driver)
        try:
            walletName = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/article/section/div/form/div[1]/div/input")))
            formEntry.send_keys_to_element(walletName, loginInfo[0])
        except TimeoutException:
            print("Could not locate login form fields")

        password = self.driver.find_element_by_xpath("/html/body/div/article/section/div/form/div[2]/div/input")
        formEntry.send_keys_to_element(password, loginInfo[1])

        passwordConfirm = self.driver.find_element_by_xpath("/html/body/div/article/section/div/form/div[3]/div/input")
        formEntry.send_keys_to_element(passwordConfirm, loginInfo[1])

        mneumonic = self.driver.find_element_by_xpath("/html/body/div/article/section/div/form/div[4]/div/input")
        formEntry.send_keys_to_element(mneumonic, loginInfo[2])

        submitButton = self.driver.find_element_by_xpath("/html/body/div/article/section/div/form/button")
        formEntry.click(on_element = submitButton)

        formEntry.perform()

        while self.driver.current_url != "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/auth/recover#3":
            continue
        
        try:
            connectButton = WebDriverWait(self.driver, 30).until(EC.presence_of_element_located((By.XPATH, "/html/body/div/article/section/div/article/div/button")))
            connectButton.click()
        except TimeoutException:
            print("Could not locate connect button")

    # Not obvious, but definitely the best way to do the job...
    def refresh(self):
        handle = self.driver.current_window_handle
        self.driver.minimize_window()
        self.driver.switch_to.window(handle)
        