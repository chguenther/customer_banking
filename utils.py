def is_float(str):
    ''' Checks whether a given string is a float.

    Args:
        str (str): The string to check.

    Returns:
        'True' if 'str' is a float.
        'False' otherwise.
    '''

    # If 'str' is a float then it contains one '.' and replacing it will leave
    # a string with only digits.
    return str.replace(".","",1).isdigit()

def calculate_balance_interest(account_balance, apr, months):
    ''' Calculates the interest earned and the updated balance.
    
    Args:
        account_balance (float): The initial account balance.
        apr (float): The annual percentage rate.
        months (int):The maturity in number of months.
        
    Returns tuple of:
        updated_account_balance (float): The updated balance equal to the
         initial balance plus interest earned.
        interest_earned (float): The amount of interest earned.
        '''
    
     # Calculate interest earned
    interest_earned = account_balance * (apr/100 * months/12)

    # Update the balance by adding the interest earned
    updated_account_balance = account_balance + interest_earned

    return updated_account_balance, interest_earned
    