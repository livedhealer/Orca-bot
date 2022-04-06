# Terrastation.py
from selenium import webdriver

class TerraStation:

    def __init__(self):
        self.driver = webdriver.Chrome(".\chromedriver.exe")

        #Might need to change this on a user to user basis too...
        self.terraStationURL = "https://station.terra.money/swap" 
        self.driver.get(self.terraStationURL)
        
        #User creds stored for plugging into website prompts when completing the swaps...
        self.username = ""
        self.password = ""


    def showAtrributes(self):
        print(self.terraStationURL,self.username, self.password)