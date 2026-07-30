n = int(input("Enter number of players: "))

name = []
runs = []
balls = []
wickets = []
sr = []

for i in range(n):
    name.append(input("Name: "))
    runs.append(int(input("Runs: ")))
    balls.append(int(input("Balls: ")))
    wickets.append(int(input("Wickets: ")))

    strike = (runs[i] / balls[i]) * 100
    sr.append(strike)

print("\nStrike Rates")
for i in range(n):
    print(name[i], "=", sr[i])

# Orange Cap
m = max(runs)
index = runs.index(m)
print("Orange Cap =", name[index])

# Purple Cap
m = max(wickets)
index = wickets.index(m)
print("Purple Cap =", name[index])

print("\nStrike Rate Above 150")
for i in range(n):
    if sr[i] > 150:
        print(name[i])

print("\nRanking by Runs")

for i in range(n):
    for j in range(i + 1, n):
        if runs[i] < runs[j]:
            runs[i], runs[j] = runs[j], runs[i]
            name[i], name[j] = name[j], name[i]

for i in range(n):
    print(i + 1, ".", name[i], "-", runs[i])