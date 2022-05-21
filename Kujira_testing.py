from Kujira import Kujira

loginInfoPath = input("Enter filepath to your loginfile something like that: ")

orca = Kujira(loginInfoPath)
input("Press enter when ready") #Need to use this time to manually click the "add wallet buttons"

# # When fully uncommented, this loop will run until you stop it - making money the whole time...

bLunaWithdrawalAmount = orca.autoWithdraw()
orca.authorizeTransaction()

print("I made it here")

