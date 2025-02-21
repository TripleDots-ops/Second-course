"""

Author:  Joseph Belda
Date written: 2/17/25
Assignment:   Assignment Part I
Short Desc:This program calculates the state and county sales tax based on
a monthly sales amount entered by the user. It uses a 5% state tax rate
and a 2.5% county tax rate, then displays the calculated tax amounts
formatted to two decimal places.   

"""

def calculate_sales_tax():
    # Constants for tax rates
    STATE_TAX_RATE = 0.05  # 5%
    COUNTY_TAX_RATE = 0.025  # 2.5%
    
    try:
        # Get total sales from user
        total_sales = float(input("Enter the total sales for the month: $"))
        
        # Input validation
        if total_sales < 0:
            print("Error: Sales amount cannot be negative.")
            return
        
        # Calculate state sales tax
        state_tax = total_sales * STATE_TAX_RATE
        
        # Calculate county sales tax
        county_tax = total_sales * COUNTY_TAX_RATE
        
        # Calculate total tax
        total_tax = state_tax + county_tax
        
        # Display results formatted to 2 decimal places
        print("\nSales Tax Calculation Summary")
        print("-" * 30)
        print(f"County Sales Tax: ${county_tax:,.2f}")
        print(f"State Sales Tax: ${state_tax:,.2f}")
        print(f"Total Sales Tax: ${total_tax:,.2f}")
        
    except ValueError:
        print("Error: Please enter a valid number for the sales amount.")

# Call the function
if __name__ == "__main__":
    calculate_sales_tax()
