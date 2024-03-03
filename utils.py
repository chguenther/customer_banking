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

def prompt_user(prompt, return_type):
    '''Prompts for user input, checks that user input is valid and returns user_input
        in a data type that corresponds to 'return_type'.

    Args:
        prompt (str): Prompt string to ask the user for input.
        return_type (str): String that defines the data type of the return variable.

    Returns:
        Variable containing user input using data type specified by 'return_type'.     
    '''

    while True:
        user_input = input(prompt)
        match return_type:
            case 'float':
                if is_float(user_input):
                    user_input = float(user_input)
                    break
                else:
                    print(f"Your input, '{user_input}', is invalid.")
            case 'int':
                if user_input.isdigit():
                    user_input = int(user_input)
                    break
                else:
                    print(f"Your input, '{user_input}', is invalid.")
            case _:
                print(f"Unknown data type, '{return_type}'.")
                exit()

    return user_input

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

    # Update the balance by adding the interest earned to the initial balance
    updated_account_balance = account_balance + interest_earned

    return updated_account_balance, interest_earned
