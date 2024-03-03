# Module 3 Challange: customer_banking
## Problem Statement

As a banking customer I want to create a savings account and a CD account by entering initial balance, annual percentage interest rate (APR), and maturity in whole months for each account. The solution must return the updated balance and the amount of interest earned for each account.

It is done when
1. I can enter initial balance, APR, and maturity for each account.
2. The solution prints out the new balance and the amount of interest earned for each account.

## Solution
### Decomposition

Tasks:
1. Prompt the user for initial balance, APR, and maturity of the savings account.
2. Create the savings account.
3. Calculate the amount of interest earned and the updated savings account balance.
4. Print the updated savings account balance and amount of interest earned.
5. Repeat steps 1 through 4 for the CD account.

### Pattern Recognition
1. The user can create two bank accounts with different account balances, APRs, and maturities for each.
2. The amount of interest earned is calculated using the following formula[^1]:
   $$
   interest\_earned = initial\_balance * (APR/100 * maturity/12)
   $$
   The new account balance is the sum of the initial account balance and the amount of interest earned.
3. The solution prints the new account balances and the amounts of interest earned in thousands notation and to two decimal places.

### Abstraction

1. The user can only create two accounts.

### Implementation
The solution consists of the following files/modules:
* `customer_banking.py`
* `savings_account.py`
* `cd_account.py`
* `Account.py`
* `utils.py`

#### Details of the `customer_banking.py` Module
`customer_banking.py` implements and calls the `main()` function.
The `main()` function 
1. Prompts the user for initial account balance, APR, and maturity of the savings account.
2. Passes these variables into the `create_savings_account` function. 
3. Prints the new account balance and the amount of interest earned in thousands format to two decimal places.
4. Repeats steps 1 through 3 for the CD account using the `create_cd_account`.

#### Details of the `savings_account.py` Module
The `savings_account.py` module implements the `create_savings_account` function called from the `customer_banking.py` module.
The `create_savings_account` function
1. Takes an account balance (`float`), APR (`float`), and maturity (`int`) as input.
2. Instantiates the `savings_account` object using the `Account` class defined in `Account.py`. The `savings_account` is created using the account balance input variable and an initial value of 0 for the amount of interest earned.
3. Calculates the amount of interest earned and the new savings account balance.
4. Returns the new savings account balance and the amount of interest earned as a tuple to the calling function.

#### Details of the `cd_account.py` Module
The `cd_account.py` module implements the `create_cd_account` function called from the `customer_banking.py` module.
The `create_cd_account` function
1. Takes an account balance (`float`), APR (`float`), and maturity (`int`) as input.
2. Instantiates the `cd_account` object using the `Account` class defined in `Account.py`. The `cd_account` is created using the account balance input variable and an initial value of 0 for the amount of interest earned.
3. Calculates the amount of interest earned and the new cd account balance.
4. Returns the new cd account balance and the amount of interest earned as a tuple to the calling function.

#### Details of the `Account.py` Module
The `Account.py` module implements the `Account` class. It has the account balance (`float`) and amount of interest earned (`float`) as attributes. It defines `set` function for account balance and the amount of interest earned.

#### Details of the `utils.py` Module
The `utils.py` module defines the following utility functions:
1. `is_float`:
   Takes a string as an input and uses the `replace` and `isdigit` python functions to detrmine whether the input string can be converted to a floating point number. Returns `True` if it can be converted and `False` if it cannot be converted.
2. `prompt_user`:
   Prompts for user input, checks that the user input is valid and returns the user input with the correct data type.
   The function takes two strings as input. The first string specifies the user prompt, the second string specifies the data type of the return value.
   It uses `is_float` if the user input is supposed to be returned as a `float`.
3. `calculate_new_balance_interest`:
    Calculates the amount of interest earned and the new balance.
    It takes the initial balance (`float`), APR (`APR`), and maturity (`int`) as inputs and returns a tuple of the new balance and the amount of interest earned.

---

## Footnotes
[^1]: I learned how to embed formulas in markdown text from GitHub Docs (2024). *Writing mathematical expressions*, https://docs.github.com/en/get-started/writing-on-github/working-with-advanced-formatting/writing-mathematical-expressions as accessed on 3/3/2024.
