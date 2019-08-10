from selenium import webdriver
from math import ceil

nc_highway_tax = .03
sticker = 10000

def calculate(apr, dp_percent):
    sticker_tax = sticker * nc_highway_tax
    down_payment = sticker * dp_percent
    apr_amount = sticker * apr

    total_loan = sticker + sticker_tax + apr_amount
    price_minus_down = total_loan - down_payment
    return price_minus_down, total_loan, down_payment

def generate_monthly_coefficient(months, apr, dp_percent):
    payment_per_month = calculate(apr, dp_percent)[0] / months
    return payment_per_month / sticker
    pass

def generate_loan_coefficient(apr, dp_percent):
    return calculate(apr, dp_percent)[1] / sticker
    pass

while True:
    monthly_payment_possible = input("\nhow much can you pay? no non-numeric characters\n")
    try:
        monthly_payment_possible = int(monthly_payment_possible)
        break
    except ValueError:
        print("\nNo! Try again!")
while True:
    months = input("\nhow many months?\n")
    try:
        months = int(months)
        break
    except ValueError:
        print("\n NO! try again!")
while True:
    actual_apr = input("\nhow much APR? examples: .065, .1, .3\n")
    try:
        actual_apr = float(actual_apr)
        break
    except ValueError:
        print("\n NO! try again!")
while True:
    actual_down = input("\nhow much do you want to put down, as a percentage? examples: .065, .1, .3\n")
    try:
        actual_down = float(actual_down)
        break
    except ValueError:
        print("\n NO! try again!")

actual_sticker = monthly_payment_possible / (generate_monthly_coefficient(months, actual_apr, actual_down) * generate_loan_coefficient(actual_apr, actual_down))
actual_down_payment = actual_sticker * actual_down
print(f"here is what you can afford: ${actual_sticker:,.2f}")
print(f"down payment: ${actual_down_payment:,.2f}")
lookup_price = str(ceil(actual_sticker))

browser = webdriver.Firefox()
browser.get("https://www.autotrader.com/cars-for-sale/Certified+Cars/cars+under+"+lookup_price+"/Pfafftown+NC-27040?searchRadius=50&zip=27040&marketExtension=true&maxPrice="+lookup_price+"&startYear=2017&maxMileage=30000&listingTypes=CERTIFIED&sortBy=relevance&numRecords=25&firstRecord=0")