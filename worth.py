
# Net worth Calculator

def get_float_input(prompt):
    """Helper function to get valid float input"""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Please enter a valid number.")

def calculate_net_worth():
    print("?? Net Worth Calculator ??")
    
    # Assets
    print("\n--- Assets ---")
    cash = get_float_input("Cash & Savings: $")
    investments = get_float_input("Investments (stocks, bonds, etc.): $")
    real_estate = get_float_input("Real Estate Value: $")
    vehicles = get_float_input("Vehicles Value: $")
    other_assets = get_float_input("Other Assets Value: $")
    
    total_assets = cash + investments + real_estate + vehicles + other_assets
    
    # Liabilities
    print("\n--- Liabilities ---")
    mortgage = get_float_input("Mortgage Balance: $")
    loans = get_float_input("Personal/Car Loans: $")
    credit_cards = get_float_input("Credit Card Debt: $")
    other_debt = get_float_input("Other Debts: $")
    
    total_liabilities = mortgage + loans + credit_cards + other_debt
    
    # Calculation
    net_worth = total_assets - total_liabilities
    
    # Results
    print("\n?? Financial Summary ??")
    print(f"Total Assets: ${total_assets:,.2f}")
    print(f"Total Liabilities: ${total_liabilities:,.2f}")
    print(f"Net Worth: ${net_worth:,.2f}")
    
    # Interpretation
    if net_worth > 0:
        print("\n?? Great job! You have a positive net worth.")
    else:
        print("\n?? Focus on debt reduction and asset growth. You've got this!")

if __name__ == "__main__":
    calculate_net_worth()

