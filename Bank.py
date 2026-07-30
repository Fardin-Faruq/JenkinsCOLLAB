n = int(input("Enter number of transactions: "))

balance = {}
deposit = 0
withdraw = 0

for i in range(n):
    acc = input("Account Number: ")
    t = input("Type (Deposit/Withdrawal): ")
    amt = int(input("Amount: "))

    if acc not in balance:
        balance[acc] = 0

    if t == "Deposit":
        balance[acc] = balance[acc] + amt
        deposit = deposit + amt
    else:
        balance[acc] = balance[acc] - amt
        withdraw = withdraw + amt

        if amt > 10000:
            print("Suspicious Withdrawal:", acc)

print("\nTotal Deposit =", deposit)
print("Total Withdrawal =", withdraw)

maxbal = -1
accno = ""

for i in balance:
    if balance[i] > maxbal:
        maxbal = balance[i]
        accno = i

print("Highest Balance Account =", accno)

print("\nFinal Balances")
for i in balance:
    print(i, "=", balance[i])