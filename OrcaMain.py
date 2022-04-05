# Orca.main.py

from Kujira import Kujira
from TerraStation import TerraStation
from selenium import webdriver

#IMPORTANT - Change this to the path for the installed driver on your own machine. I wonder if there's a way to include this in the repo...
chromeDriverPath = "./chromedriver.exe"

driver = webdriver.Chrome(chromeDriverPath)

terra = TerraStation(driver)
orca = Kujira(driver)
orca.showAtrributes()

