name = ["Virat", "Rohit", "Bumrah"]

runs = [80, 60, 20]
balls = [50, 30, 18]
wickets = [1, 0, 5]

sr = []

for i in range(len(name)):
    strike = (runs[i] / balls[i]) * 100
    sr.append(strike)

print("Strike Rates")
for i in range(len(name)):
    print(name[i], "=", round(sr[i], 2))

m = max(runs)
index = runs.index(m)
print("\nOrange Cap =", name[index])

m = max(wickets)
index = wickets.index(m)
print("Purple Cap =", name[index])

print("\nPlayers with Strike Rate above 150")
for i in range(len(name)):
    if sr[i] > 150:
        print(name[i])

print("\nRanking by Runs")

for i in range(len(runs)):
    for j in range(i + 1, len(runs)):
        if runs[i] < runs[j]:
            runs[i], runs[j] = runs[j], runs[i]
            name[i], name[j] = name[j], name[i]

for i in range(len(name)):
    print(i + 1, ".", name[i], "-", runs[i])