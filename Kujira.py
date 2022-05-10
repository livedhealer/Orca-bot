# Kujira.py

from selenium import webdriver
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.common.exceptions import StaleElementReferenceException
from selenium.webdriver.chrome.options import Options 
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class Kujira:
    
    def __init__(self, fileLocation):
        self.fileLocation = fileLocation
        self.password = ""
        self.secondTab = "secondtab"
        self.bLunaWithdrawThresholdAmount = 0 # By default... Code below will alter this so as to not lose money on small transactions
        self.terraStationExtensionHomeURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#"
        self.terraStationExtensionLoginURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/auth/recover"
        self.bLunaMarketURL = "https://orca.kujira.app/markets/terra/anchor/bLuna"
        
        addPluginOption = self.addTerraStationPlugin()
        # Kickstart the webdriver and add the Terra Station plugin
        self.driver = webdriver.Chrome(".\chromedriver.exe", options=addPluginOption) #Use Chrome...
        self.driver.get(self.terraStationExtensionLoginURL)
        self.addTerraStationPlugin()

        #Login to the wallet
        self.initializeWallet()
        self.driver.get(self.terraStationExtensionHomeURL)

        # Save the handle of this first tab so we can switch to it later
        self.firstTab = self.driver.current_window_handle
  
        # Lets open Kujira in the second tab
        self.driver.execute_script("window.open('about:blank', 'secondtab');")
        self.driver.switch_to.window(self.secondTab)
        self.driver.get(self.bLunaMarketURL) #Pop open a tab to the bLuna collateral market...

        #!!!!!ADD MICHAEL'S OLD FUNCTIONS HERE
        
        #Need to prompt the user to make sure their Terra Station Wallet is connected at this point
        #Also prompt the user to choose their premium discount, bid amount, and percentage
        #Once user confirms their input is good to go, init is done!
        #Instead of manual input, we could automate that stuff in the future when we get better with Selenium, but not yet...


    #Bread and butter of this class... Check for nonzero amount of bLuna to withdraw, and if nonzero, SMASH that withdraw button!
    def autoWithdraw(self):
        print("Michael is gonna build me!")

        self.driver.implicitly_wait(3) #Identified as the method to get button to be clicked


        #self.driver.maximize_window()

        value = "0.000000"      
        
        bean_counter = 0

        #While loop to check the value of Kujira and click withdrawal
        while value == "0.000000":
            
            firstzero = self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/h3/div/span[1]')

            secondzero = self.driver.find_element_by_xpath ('/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/h3/div/span[2]')        

            zeronumber = str(firstzero.text)
            
            zeronumber2 = str(secondzero.text)

            bean_counter += 1

            value = (zeronumber + zeronumber2)
            if (bean_counter == 150):
                print("Damn")
                bean_counter = 0        
        
        print("KABOOOOOOOOOOOOM!!!!! We got something")
        withdrawal = self.driver.find_element_by_xpath('/html/body/div[1]/div/div[3]/div[2]/div/div/div[2]/button')
        withdrawal.click()

        #WE NEED TO FIGURE OUT HOW TO INTERACT WITH THE TERRA STATION POPUP THAT OCCURS HERE......

        return value


    #This would allow us to automatically re-invest our earnings without a human to baby-sit the computer after making a withdrawal and Terra Station swaps to a stable coin.
    def autoBid(self):
        print("Michael might build me!")

        #There are at least 2x confirmation popups that occur from Terra Station when this method runs...

       
    # def wallet(self):
    #     print("Sah dude?    'Dude' or 'Sah'?")

    #     choice = input("> ")
            
    #     if "Dude" in choice:
    #         self.UserInput()
    #     elif "Sah" in choice:
    #         self.wallet()
    #     else:
    #          print("Brah, what?")
        
    # def UserInput(self):
    #     print("Dude Sah?    'Dude' or 'Sah'?")

    #     choice = input("> ")

    #     if "Dude" in choice:
    #         print("LEGGO")
    #     elif "Sah" in choice:
    #         print("PeePee")
    #     else:
    #         print("Yeet")

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


    #This method authorizes Kujira transactions! It assumes that Terra Station is still open and logged in at the first tab
    def authorizeTransaction(self):

        self.driver.switch_to.window(self.firstTab)
        self.driver.get(self.terraStationExtensionHomeURL)

        # self.driver.implicitly_wait(3)

        # passwordBox = self.driver.find_element_by_xpath("/html/body/div[1]/article/section/div/div/form/div[1]/div/div/input")
        # print("passwordBox.text = " + passwordBox.text)
        #Get ahold of the password box and input our password... Keep trying if we don't immediately find it.
        while True:
            try:                                                                                            
                passwordBox = WebDriverWait(self.driver, 2).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/article/section/div/div/form/div[1]/div/div/input")))
                break
            except TimeoutException:
                print("Could not locate post transaction form fields. Trying again...")
                self.driver.get(self.terraStationExtensionHomeURL)

        #Setup an action chain to fill the form
        yeetPassword = ActionChains(self.driver)
        yeetPassword.send_keys_to_element(passwordBox, self.password)
        yeetPassword.perform()


        try:
            # Find and click the post button                                                                                            
            postButton = WebDriverWait(self.driver, 4).until(EC.presence_of_element_located((By.XPATH, "/html/body/div[1]/article/section/div/div/form/div[2]/button[2]")))
            postButton.click()
        except TimeoutException:
            print("Could not locate transaction post button...")
            self.driver.get(self.terraStationExtensionHomeURL)
        except StaleElementReferenceException:
            print("Weird exception... postButton still clicked. Press on in this one case!")