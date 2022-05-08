# Orca.main.py

from Kujira import Kujira
from Terrastation import TerraStation
import time

terra = TerraStation()
time.sleep(15) #Need to use this time to manually add bLuna to the list in Terra Station

orca = Kujira()
time.sleep(20) #Need to use this time to manually click the "add wallet buttons"

print("HERE WE GO!!!!!!!!!!!!!!!!!")

# When fully uncommented, this loop will run until you stop it - making money the whole time...
# while True: 
bLunaWithdrawalAmount = orca.autoWithdraw()
orca.authorizeTransaction()

print("I made it here")

terra.swap("bLuna", bLunaWithdrawalAmount, "Luna")
terra.swap("Luna", terra.lunaIntermediateAmount, "UST")
#orca.autobid()


