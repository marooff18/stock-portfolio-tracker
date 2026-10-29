import csv
# Stock Portfolio Tracker

stock_prices = {
    "TCS": 3500,
    "INFY": 1500,
    "RELIANCE": 2500,
    "HDFCBANK": 1700,
    "ITC": 450
}

# Store the user's portfolio
portfolio = {}

total_investment = 0

print("===== STOCK PORTFOLIO TRACKER =====")
print("Available stocks:", ", ".join(stock_prices.keys()))

number_of_stocks = int(input("How many different stocks do you want to enter? "))

for i in range(number_of_stocks):

    stock_name = input("\nEnter stock name: ").upper()

    if stock_name not in stock_prices:
        print("Stock not found! Please try again.")
        continue

    quantity = int(input("Enter quantity: "))

    if quantity <= 0:
        print("Quantity must be greater than zero.")
        continue

    price = stock_prices[stock_name]

    investment = price * quantity

    portfolio[stock_name] = portfolio.get(stock_name, 0) + quantity

    total_investment += investment

    print("Investment value: ₹", investment)


# Display portfolio summary

print("\n===== PORTFOLIO SUMMARY =====")

for stock_name, quantity in portfolio.items():

    price = stock_prices[stock_name]

    investment = price * quantity

    print(
        stock_name,
        "| Quantity:", quantity,
        "| Price: ₹", price,
        "| Investment: ₹", investment
    )

print("\nTotal Portfolio Investment: ₹", total_investment)
# Ask the user whether to save the portfolio

save_choice = input("Do you want to save the portfolio? (yes/no): ").lower()

if save_choice == "yes":

    with open("portfolio.csv", "w", newline="") as file:

        writer = csv.writer(file)

        writer.writerow(["Stock Name", "Quantity", "Price Per Share", "Investment Value"])

        for stock_name, quantity in portfolio.items():

            price = stock_prices[stock_name]

            investment = price * quantity

            writer.writerow([stock_name, quantity, price, investment])

        writer.writerow([])
        writer.writerow(["Total Investment", "", "", total_investment])

    print("Portfolio saved successfully!")






