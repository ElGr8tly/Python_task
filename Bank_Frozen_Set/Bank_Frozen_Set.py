# Define initial account balances
account_balances = {
    "Mohamed": 5000,
}

# Define a set of allowed transactions
ALLOWED_TRANSACTIONS = frozenset(["deposit", "withdraw"])

# Define a function to perform transactions on accounts
def perform_transaction(account_name, transaction_type, amount):
    if transaction_type not in ALLOWED_TRANSACTIONS:
        print("Transaction type not allowed.")
        return
    
    if account_name not in account_balances:
        print("Account ",account_name,"not found.")
        return
    else :
        print("Account ",account_name," is found.")
    if transaction_type == "deposit":
        account_balances[account_name] += amount
        print(f"Deposit of {amount} successful. New balance: {account_balances[account_name]}")
    elif transaction_type == "withdraw":
        if amount > account_balances[account_name]:
            print("Insufficient balance.")
        else:
            account_balances[account_name] -= amount
            print(f"Withdrawal of {amount} successful. New balance: {account_balances[account_name]}")


# Print the updated dictionary
print(account_balances)
perform_transaction("John", "deposit", 2000)
perform_transaction("Mohamed", "withdraw", 2000)
print(account_balances)