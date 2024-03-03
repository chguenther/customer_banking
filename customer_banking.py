# Import the is_float function from utils to check input
from utils import prompt_user

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
    savings_balance = prompt_user("Please enter the savings account balance.\n", "float")
    savings_interest = prompt_user("Please enter the savings account interest rate.\n", "float")
    savings_maturity = prompt_user("Please enter the savings account maturity in months.\n", "int")

    # Call the create_savings_account function and pass the variables from the user.
    updated_savings_balance, savings_interest_earned = create_savings_account(savings_balance, savings_interest, savings_maturity)

    # Print out the interest earned and updated savings account balance with interest earned for the given months.
    print("-" * 80)
    print(f"The updated savings account balance is ${updated_savings_balance:,.2f}.")
    print(f"The amount of interest earned over {savings_maturity} months with an APR of {savings_interest:.2f}% is ${savings_interest_earned:,.2f}")
    print("=" * 80)

    # Prompt the user to set the CD balance, interest rate, and months for the CD account.
    cd_balance = prompt_user("Please enter the CD account balance.\n", "float")
    cd_interest = prompt_user("Please enter the CD account interest rate.\n", "float")
    cd_maturity = prompt_user("Please enter the CD account maturity in months.\n", "int")

    # Call the create_cd_account function and pass the variables from the user.
    updated_cd_balance, cd_interest_earned = create_cd_account(cd_balance, cd_interest, cd_maturity)

    # Print out the interest earned and updated CD account balance with interest earned for the given months.
    print("-" * 80)
    print(f"The updated CD account balance is ${updated_cd_balance:,.2f}.")
    print(f"The amount of interest earned over {cd_maturity} months with an APR of {cd_interest:.2f}% is ${cd_interest_earned:,.2f}")
    print("=" * 80)

if __name__ == "__main__":
    # Call the main function.
    main()