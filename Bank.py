
n = int(input("Enter number of transactions: "))

balances = {}
total_deposit = 0
total_withdrawal = 0

for i in range(n):
    print(f"\nTransaction {i+1}")
    acc = input("Account Number: ")
    t = input("Type (Deposit/Withdrawal): ").lower()
    amount = float(input("Amount: "))

    if acc not in balances:
        balances[acc] = 0

    if t == "deposit":
        balances[acc] += amount
        total_deposit += amount

    elif t == "withdrawal":
        balances[acc] -= amount
        total_withdrawal += amount

        if amount > 10000:
            print("Suspicious Withdrawal:", acc, "-", amount)


highest_account = max(balances, key=balances.get)

print("\n------ REPORT ------")
print("Total Deposits:", total_deposit)
print("Total Withdrawals:", total_withdrawal)
print("Highest Balance Account:", highest_account)
print("Balance:", balances[highest_account])

print("\nFinal Balances")
for acc, bal in balances.items():
    print(acc, ":", bal)