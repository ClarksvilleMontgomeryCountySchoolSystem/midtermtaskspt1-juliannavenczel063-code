balance = starting_balance
balance -= withdrawal_amount

balance -= atm_fee

total_monthly_fees = monthly_fee * months_inactive
balance -= total_monthly_fees

full_twenties = balance//20
remaining_dollars = balance%20

print(f"Account Holder: {account_holder}")
print(f"Remaining Balance: ${balance}")
print(f"Full $20 Bills: {full_twenties}")
print(f"Remaining Dollars: ${remaining_dollars}")
