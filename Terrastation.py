# Terrastation.py
class TerraStation:

    #Might need to change this on a user to user basis too...
    terraStationWalletExtensionURL = "chrome-extension://aiifbnbfobpmeekipheeijimdpnlpgpp/index.html#/"

    #User auth...
    terraUsername = ""
    terraPassword = ""

    def __init__(self, driver):
        self.driver = driver #Use previously opened Chrome tab if possible...  TEST THIS!!!!!




    def showAtrributes(self):
        print(self.chromeDriverPath, self.terraStationWalletExtensionURL)