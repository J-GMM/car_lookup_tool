from math import ceil
from selenium import webdriver


def calculate_finances(apr, dp_percent):
    base_sticker_tax = base_sticker_price * highway_tax
    down_payment = base_sticker_price * dp_percent
    apr_amount = base_sticker_price * apr

    total_loan = base_sticker_price + base_sticker_tax + apr_amount
    price_minus_down = total_loan - down_payment
    return price_minus_down, total_loan, down_payment


def monthly_multiplier(months, apr, dp_percent):
    payment_per_month = calculate_finances(apr, dp_percent)[0] / months
    return payment_per_month / base_sticker_price


def loan_multiplier(apr, dp_percent):
    return calculate_finances(apr, dp_percent)[1] / base_sticker_price


# Creates a table of questions, storing user input.
def get_input_values():
    print("Please enter the following information, without dollar signs.")
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
                print("\nUnrecognized input - please try again.")
    return messages

highway_tax = .03
base_sticker_price = 10000

# Get the table of questions and values.
values = get_input_values()

# Get the affordable sticker price from the values input by the user.
affordable_sticker_price = values[1][0] / (
            monthly_multiplier(values[1][1], values[1][2], values[1][3]) * loan_multiplier(
        values[1][2], values[1][3]))
affordable_down_payment = affordable_sticker_price * values[1][3]
print(f"Affordable Sticker Price: ${affordable_sticker_price:,.2f}\nDown Payment: ${affordable_down_payment:,.2f}")
lookup_price = str(ceil(affordable_sticker_price))

continue_confirmation = input("\nContinue with a car search online using this information?\n Enter N for no."
                              "\nTo continue, simply press enter.")
if continue_confirmation.lower() == "n":
    quit(0)

# Gather basic location information for the web search.
location = input("Enter city and state (two letter state abbreviation), separated by a comma. Ex. Wichita,KS\n")
city, state = location.split(",")
zip = input("Enter ZIP code for search.\n")

# Open Chromedriver to search for the cars on Autotrader.
print("Looking for cars ... ")
browser = webdriver.Chrome()
browser.maximize_window()
browser.get(("https://www.autotrader.com/cars-for-sale/Certified+Cars/cars+under+{price}/"
             "{city}+{state}-{zip}?listingTypes=CERTIFIED&searchRadius=25&zip={zip}&marketExtension=include&"
             "maxPrice={price}&isNewSearch=true&sortBy=relevance&numRecords=25&firstRecord=0")\
             .format(price=lookup_price, zip=zip, city=city, state=state))
