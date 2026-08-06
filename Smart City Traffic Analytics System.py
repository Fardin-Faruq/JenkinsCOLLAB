roads = [
    {"id":"J101","city":"Chennai","vehicle":800,"speed":25,"accident":4},
    {"id":"J102","city":"Bangalore","vehicle":600,"speed":40,"accident":2},
    {"id":"J103","city":"Hyderabad","vehicle":950,"speed":20,"accident":5},
    {"id":"J104","city":"Kochi","vehicle":500,"speed":50,"accident":1}
]

for road in roads:
    road["score"] = road["vehicle"] + road["accident"]*100 - road["speed"]

print("scores")
for road in roads:
    print(road["id"],road["score"])

for i in range(len(roads)):
    for j in range(i+1,len(roads)):
        if roads[i]["score"] < roads[j]["score"]:
            roads[i],roads[j] = roads[j],roads[i]

print("rank")
count = 1
for road in roads:
    print(count,road["id"])
    count = count + 1

print("alerts")
for road in roads:
    if road["score"] > 1000:
        print(road["id"])

city = {}

for road in roads:
    if road["city"] in city:
        city[road["city"]] = city[road["city"]] + road["score"]
    else:
        city[road["city"]] = road["score"]

print("city")
for i in city:
    print(i,city[i])

print("top 5")
for i in range(len(roads)):
    if i < 5:
        print(roads[i]["id"],roads[i]["score"])

file = open("traffic.txt","w")

for road in roads:
    file.write(road["id"]+" "+str(road["score"])+"\n")

file.close()

file = open("traffic.txt","r")

print("file")

for line in file:
    print(line.strip())

file.close()
