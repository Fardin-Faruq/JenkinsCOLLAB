players = []

n = int(input("Enter number of players: "))

for i in range(n):
    print(f"\nPlayer {i+1}")

    name = input("Name: ")
    runs = int(input("Runs: "))
    balls = int(input("Balls Faced: "))
    wickets = int(input("Wickets: "))

    strike_rate = (runs / balls) * 100

    players.append({
        "name": name,
        "runs": runs,
        "balls": balls,
        "wickets": wickets,
        "strike_rate": strike_rate
    })

# Orange Cap
orange = max(players, key=lambda x: x["runs"])

# Purple Cap
purple = max(players, key=lambda x: x["wickets"])

print("\nStrike Rates")
for p in players:
    print(p["name"], ":", round(p["strike_rate"], 2))

print("\nOrange Cap Winner:", orange["name"], "-", orange["runs"], "runs")
print("Purple Cap Winner:", purple["name"], "-", purple["wickets"], "wickets")

print("\nPlayers with Strike Rate above 150")
for p in players:
    if p["strike_rate"] > 150:
        print(p["name"], "-", round(p["strike_rate"], 2))

print("\nRanking by Runs")
players.sort(key=lambda x: x["runs"], reverse=True)

rank = 1
for p in players:
    print(rank, ".", p["name"], "-", p["runs"], "runs")
    rank += 1