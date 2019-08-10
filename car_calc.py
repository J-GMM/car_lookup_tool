from math import ceil

from selenium import webdriver

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


def get():
    x = 0
    messages = [["\nMonthly Payment?\n", "\nLoan length in months?\n",
                 "\nPercent APR?\n",
                 "\nPercent Down?\n"], []]

    for x in range(0, len(messages[0])):
        while True:
            messages[1].append(input(messages[0][x]))
            try:
                messages[1][x] = float(messages[1][x])
                if x >= 2:
                    if messages[1][x] > 1:
                        messages[1][x] = messages[1][x] / 100
                break
            except ValueError:
                print("\nNo! Try again!")
    return messages


values = get()

actual_sticker = values[1][0] / (
            generate_monthly_coefficient(values[1][1], values[1][2], values[1][3]) * generate_loan_coefficient(
        values[1][2], values[1][3]))
actual_down_payment = actual_sticker * values[1][3]
print(f"Affordable Sticker Price: ${actual_sticker:,.2f}\nDown Payment: ${actual_down_payment:,.2f}")
lookup_price = str(ceil(actual_sticker))
print("Looking for cars ... ")

browser = webdriver.Firefox()
browser.get("https://www.autotrader.com/cars-for-sale/Certified+Cars/cars+under+"+lookup_price+"/Pfafftown+NC-27040?searchRadius=50&zip=27040&marketExtension=true&maxPrice="+lookup_price+"&startYear=2017&maxMileage=30000&listingTypes=CERTIFIED&sortBy=relevance&numRecords=25&firstRecord=0")