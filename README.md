# Orca-bot: Automating Liquidated Crypto Purchases
## Background
The Kujira Orca platform offers a unique opportunity for investors by providing discounted sales of cryptocurrencies that have been posted as collateral on liquidated loans. These discounts are not only significant, often exceeding 3% on daily and weekly liquidations, but they also present a lucrative opportunity for those looking to capitalize on these moments. The challenge, however, lies in the volatility of the crypto market. The Orca-bot aims to mitigate this by quickly converting volatile assets into stable assets pegged to fiat currencies, thus reducing the exposure to crypto market fluctuations to mere milliseconds.

## Project Goal
The primary challenge in leveraging the Kujira Orca platform's opportunities is the lack of an easily accessible API for both Kujira and the Terra Station Wallet, which it utilizes. To overcome this, our project has set out to:

- Automate the web interface and HTTP calls of the Terra Station crypto wallet and its browser extension, bypassing the need for a direct API.
Employ the Python selenium module to automate operations within the Terra Station crypto wallet and its browser extension, facilitating automated transactions.
- Utilize selenium for monitoring and interacting with the Kujira platform to identify and initiate purchase opportunities efficiently.

## Results
- The project has achieved successful end-to-end automation of the purchase and transaction process, demonstrating its effectiveness just in time before the unfortunate crash of Luna. This milestone marks a significant achievement in our journey to automate and capitalize on liquid crypto purchases.

## Current State
- With the Terra2.9.0_0.crx browser extension installed and the execution of both the OrcaMain.py and Terrastation.py scripts—after inputting account credentials into the provided template text file—the program was capable of autonomously processing liquidation bids based on user-configured settings. Following a successful bid, the program automatically converted the acquired cryptocurrency into a USD stablecoin throughout the day.

- To date, the system has been tested with small amounts of fiat currency, showing promising results. However, further testing is required to ensure its reliability and effectiveness before deploying significant investments.

- *The project was halted due to the Luna/Terra ecosystem collapse. TerraStation and Kujira both have been updated, and the current scripts will need overhauls to function with these updates. Terra and Kujira have both been improved and largely rebuilt, so the financial opportunity is likely back again if a dev were to take up the mantle again...*

Note to Users
This project is in continuous development, and we welcome contributions and feedback from the community. 