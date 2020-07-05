# Car Lookup Tool
Accepts user input, calculates affordable car price and down payment, then performs a search on Autotrader for cars for sale under the calculated price.

## Setup
Simply clone, install the required packages using `pip install -r requirements.txt`. 

Ensure the appropriate Chromedriver for your chrome version is downloaded from
https://chromedriver.chromium.org/downloads. Run the script using python.


## Usage
The script asks for your requested monthly payment, requested length of loan in months, qualified percent APR, and what percent you are ready to put down. It then gives you a sticker price and down payment affordable according to your input. 

After confirmation to continue and asking for location information, the script opens a Chrome window to perform a search on Autotrader.com with location and price terms. 