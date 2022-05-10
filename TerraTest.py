# Orca.main.py

from Kujira import Kujira
from Terrastation import TerraStation

loginInfoPath = input("Type the filepath of your wallet login info file and press enter: ")

terra = TerraStation(loginInfoPath)
input("Press enter when ready") #Need to use this time to manually add bLuna to the list in Terra Station

terra.swap("Luna", "MAX", "UST")
input("press enter to continue after swapping a little to test the refresh method...")
terra.swap("Luna", "MAX", "UST")

