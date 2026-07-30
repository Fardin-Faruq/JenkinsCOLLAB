balance = {}

transactions = [
    ["101", "Deposit", 15000],
    ["102", "Deposit", 8000],
    ["101", "Withdrawal", 12000],
    ["103", "Deposit", 5000]
]

deposit = 0
withdraw = 0

for t in transactions:
    acc = t[0]
    typ = t[1]
    amt = t[2]

    if acc not in balance:
        balance[acc] = 0

    if typ == "Deposit":
        balance[acc] += amt
        deposit += amt
    else:
        balance[acc] -= amt
        withdraw += amt

        if amt > 10000:
            print("Suspicious Withdrawal:", acc)

print("Total Deposit =", deposit)
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