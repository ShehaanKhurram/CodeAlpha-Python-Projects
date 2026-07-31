Stock_Prices = {
    "AAPL": 180,
    "TSLA": 250,
    "GOOGL": 140,
    "MSFT": 330,
    "AMZN": 145
}

def show_available_stocks():
    print("\nAvailable Stocks: ")
    for stock, price in Stock_Prices.items():
        print(f"{stock:<5} -> {price}")
    print("\n")

def get_portfolio():
    portfolio = {}

    print("Enter stock name and quantity(type 'done' when you want to finish): ")

    while True:
        stock = input("Stock Symbol: ").upper().strip()

        if stock == "DONE":
            break

        if stock not in Stock_Prices.keys():
            print(f"{stock} not found! Please try to enter one of these: {', '.join(Stock_Prices.keys())}")
            continue

        quantity_input = input(f"Enter quantitiy of {stock}: ").strip()

        if not quantity_input.isdigit() or int(quantity_input) <= 0:
            print("Error: Please enter valid positive input number for quantity.")
            continue

        quantity = int(quantity_input)

        if stock in portfolio.keys():
            portfolio[stock] += quantity
        else:
            portfolio[stock] = quantity

        print(f"Added {quantity} of {stock} in portfolio successfully!\n")

    return portfolio

def calculate_investment(portfolio):
    breakdown = {}
    total = 0

    for stock, quantity in portfolio.items():
        value = Stock_Prices[stock] * quantity
        breakdown[stock] = value
        total += value

    return breakdown, total


def display_summary(breakdown, total):
    print("\n" + "=" * 40)
    print("        PORTFOLIO SUMMARY")
    print("=" * 40)
    print(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}")

    for stock, value in breakdown.items():
        qty = value // Stock_Prices[stock]
        print(f"{stock:<8}{qty:<8}${Stock_Prices[stock]:<9}${value:<10}")
 
    print("-" * 40)
    print(f"TOTAL INVESTMENT: ${total}")
    print("=" * 40)

def save_to_file(breakdown, total, username):
    
    filename = username + "'s_portfolio.txt"
    
    try:
        with open(filename, "w") as file:
            file.write("      STOCK PORTFOLIO TRACKER\n")
            file.write("=" * 40 + "\n")
            file.write(f"{'Stock':<8}{'Qty':<8}{'Price':<10}{'Value':<10}\n")

            for stock, value in breakdown.items():
                qty = value // Stock_Prices[stock]
                file.write(f"{stock:<8}{qty:<8}${Stock_Prices[stock]:<9}${value:<10}\n")
                
            file.write("-" * 40 + "\n")
            file.write(f"TOTAL INVESTMENT: ${total}\n")
            file.write("=" * 40 + "\n")

        print(f"Summary saved to '{filename}'")
    except IOError as e:
        print(f"Could not save file: {e}")

print("__________Welcome toaa Stock Portfolio Tracker__________")

show_available_stocks()
portfolio = get_portfolio()

if not portfolio:
    print("No Stocks Entered! exiting...")
else:    
    print(f"Your portfolio: {portfolio}")

breakdown, total = calculate_investment(portfolio)

display_summary(breakdown, total)

user_input = input("Do you want to save your portfolio in a file? (y/n): ").lower().strip()

if user_input == "y":
    
    while True:
        username = input("Enter your name: ").lower().strip()
        
        if not username.isalpha():
            print("Invalid input. Please try again!")
            continue
        else:
            break
        
    save_to_file(breakdown, total, username)

print("Thanks for using Stock Portfolio Tracker!\nprogress...\nprogress...\nexit successfully...")