# Orca-bot
Bot for Liquid Crypto Purchases

# TODO:

## Michael: 
- [] Implement clicking and form data entry for Kujira.autobid()
- [x] Manually try at least one bid (just to get the flow down)
- [] Add any extra Kujira button-clicking as needed
- [] Add proper logging-to-file throughout Kujira.py and OrcaMain.py (see https://realpython.com/python-logging/)
- [] Put every critical find_element call in Kujira within a try-catch structure, and catch defined exceptions

## Connor:
- [x] Add auto-setup script for Terra Station
- [x] Add handler for Terra Station Popups during Kujira transactions
- [x] Put critical find_element calls in Terrastation within a try-catch structure, and catch exceptions
- [] Make Kujira fail-safe method
- [] Make Terra station fail-safe method
- [] Make our Terrastation and Kujira classes children of a parent class (so we they can share helper methods)
