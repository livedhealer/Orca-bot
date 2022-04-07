# Kujira.py
from selenium import webdriver

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

    #This would allow us to automatically re-invest our earnings without a human to baby-sit the computer after making a withdrawal and Terra Station swaps to a stable coin.
    def autoBid(self):
        print("Michael might build me!")

    def showAtrributes(self):
        print(self.chromeDriverPath, self.bLunaMarketURL)

    #!!!!!ADD MICHAEL'S OLD FUNCTIONS HERE

    
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