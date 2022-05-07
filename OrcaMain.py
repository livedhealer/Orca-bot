# Orca.main.py

from Kujira import Kujira
from Terrastation import TerraStation

terra = TerraStation()
orca = Kujira()

#This loop will run until you stop it - making money the whole time...
#while True: 
bLunaWithdrawalAmount = orca.autoWithdraw()
#bLunaWithdrawalAmount = .0001 # Use this line for testing
# terra.swap("bLuna", bLunaWithdrawalAmount, "Luna")
# terra.swap("Luna", terra.lunaIntermediateAmount, "UST")
#orca.autobid()


