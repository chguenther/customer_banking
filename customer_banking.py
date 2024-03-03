# Import the is_float function from utils to check input
from utils import is_float

# Import the create_cd_account and create_savings_account functions
from savings_account import create_savings_account
from cd_account import create_cd_account

# Define the main function
def main():
    """This function prompts the user to enter the savings and cd account balance, interest rate,
    and the length of months to determine the interest gained.
    It displays the interest earned on the savings and CD accounts and updates the balances.
    """
    # Prompt the user to set the savings balance, interest rate, and months for the savings account.
    while True:
        savings_balance = input("Please enter the savings account balance.\n")
        if is_float(savings_balance):
            savings_balance = float(savings_balance)
            break
        else:
            print(f"Your savings account balance, '{savings_balance}', is invalid.")

    while True:
        savings_interest = input("Please enter the interest rate on the savings account.\n")
        if is_float(savings_interest):
            savings_interest = float(savings_interest)
            break
        else:
            print(f"Your savings interest rate, '{savings_interest}', is invalid.")

    while True:
        savings_maturity = input("Please enter the savings account maturity in months.\n")
        if savings_maturity.isdigit():
            savings_maturity = int(savings_maturity)
            break
        else:
           print(f"Your savings account maturity, '{savings_maturity}', is invalid.") 

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("-" * 60)
    print(f"The updated savings account balance is ${updated_savings_balance:,.2f}.")
    print(f"The amount of interest earned over {savings_maturity} months is ${savings_interest_earned:,.2f}")
    print("=" * 60)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    while True:
        cd_balance = input("Please enter the CD account balance.\n")
        if is_float(cd_balance):
            cd_balance = float(cd_balance)
            break
        else:
            print(f"Your CD account balance, '{cd_balance}', is invalid.")

    while True:
        cd_interest = input("Please enter the interest rate on the CD account.\n")
        if is_float(cd_interest):
            cd_interest = float(cd_interest)
            break
        else:
            print(f"Your savings interest rate, '{cd_interest}', is invalid.")

    while True:
        cd_maturity = input("Please enter the CD account maturity in months.\n")
        if cd_maturity.isdigit():
            cd_maturity = int(cd_maturity)
            break
        else:
           print(f"Your savings account maturity, '{cd_maturity}', is invalid.")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("-" * 60)
    print(f"The updated CD account balance is ${updated_cd_balance:,.2f}.")
    print(f"The amount of interest earned over {cd_maturity} months is ${cd_interest_earned:,.2f}")
    print("=" * 60)

if __name__ == "__main__":
    # Call the main function.
    main()