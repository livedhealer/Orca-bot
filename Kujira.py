# Kujira.py
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

class Kujira:
    
    def __init__(self):
        self.bLunaMarketURL = "https://orca.kujira.app/markets/terra/anchor/bLuna"
        self.driver = webdriver.Chrome(".\chromedriver.exe") #Use Chrome...
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


        self.driver.maximize_window()

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
        
        print("KABOOOOOOOOOOOOM!!!!! First live fire exercise is a success...")
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