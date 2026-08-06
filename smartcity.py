roads = [
    {"id":"J101","city":"Chennai","vehicle":800,"speed":25,"accident":4},
    {"id":"J102","city":"Bangalore","vehicle":600,"speed":40,"accident":2},
    {"id":"J103","city":"Hyderabad","vehicle":950,"speed":20,"accident":5},
    {"id":"J104","city":"Kochi","vehicle":500,"speed":50,"accident":1}
]

for road in roads:
    road["score"] = road["vehicle"] + road["accident"] * 100 - road["speed"]

print("Congestion Score")
for road in roads:
    print(road["id"], road["city"], road["score"])

for i in range(len(roads)):
    for j in range(i + 1, len(roads)):
        if roads[i]["score"] < roads[j]["score"]:
            roads[i], roads[j] = roads[j], roads[i]

print("\nRanking")
rank = 1
for road in roads:
    print(rank, road["id"], road["city"], road["score"])
    rank = rank + 1

print("\nTraffic Alert")
for road in roads:
    if road["score"] > 1000:
        print(road["id"], "Heavy Traffic")

city = {}

for road in roads:
    if road["city"] in city:
        city[road["city"]] = city[road["city"]] + road["score"]
    else:
        city[road["city"]] = road["score"]

print("\nCity Report")
for name in city:
    print(name, city[name])

print("\nTop 5 Roads")
for i in range(len(roads)):
    if i < 5:
        print(roads[i]["id"], roads[i]["city"], roads[i]["score"])

file = open("traffic.txt","w")

for road in roads:
    file.write(road["id"] + " " + road["city"] + " " + str(road["score"]) + "\n")

file.close()

print("\nReading File")

file = open("traffic.txt","r")

for line in file:
    print(line.strip())

file.close()