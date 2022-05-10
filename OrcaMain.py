# Orca.main.py

from Kujira import Kujira
from Terrastation import TerraStation

loginInfoPath = input("Type the filepath of your wallet login info file and press enter: ")

terra = TerraStation(loginInfoPath)
input("Press enter when ready") #Need to use this time to manually add bLuna to the list in Terra Station

orca = Kujira(loginInfoPath)
input("Press enter when ready") #Need to use this time to manually click the "add wallet buttons"

# # When fully uncommented, this loop will run until you stop it - making money the whole time...
while True: 
    bLunaWithdrawalAmount = orca.autoWithdraw()
    orca.authorizeTransaction()

    print("I made it here")

    terra.swap("bLuna", bLunaWithdrawalAmount, "Luna")
    terra.swap("Luna", terra.lunaIntermediateAmount, "UST")
#orca.autobid()


