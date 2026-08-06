faculty = [
    {"id":"F101","name":"Rahul","dept":"CSE","pub":40,"h":20,"budget":150000,"collab":80},
    {"id":"F102","name":"Priya","dept":"ECE","pub":30,"h":15,"budget":90000,"collab":70},
    {"id":"F103","name":"Arjun","dept":"MECH","pub":50,"h":25,"budget":180000,"collab":90}
]

for person in faculty:
    if person["budget"] < 0:
        print("Invalid Budget")
    person["score"] = 0.4 * person["pub"] + 0.3 * person["h"] + 0.3 * person["collab"]
    person["grant"] = person["budget"]

print("Faculty getting grant above 100000")
for person in faculty:
    if person["grant"] > 100000:
        print(person["name"], person["grant"])

dept_fund = {}

for person in faculty:
    dept = person["dept"]
    if dept in dept_fund:
        dept_fund[dept] += person["grant"]
    else:
        dept_fund[dept] = person["grant"]

print("Department with Maximum Funding")
print(max(dept_fund, key=dept_fund.get))

faculty.sort(key=lambda person: person["score"], reverse=True)

print("Faculty Ranking")
rank = 1
for person in faculty:
    print(rank, person["name"], person["score"])
    rank += 1

total_score = 0

for person in faculty:
    total_score += person["score"]

average_score = total_score / len(faculty)
print("Average Research Score =", average_score)

print("Top Performer =", faculty[0]["name"])

file = open("ranking.txt", "w")

for person in faculty:
    file.write(person["name"] + " " + str(person["score"]) + "\n")

file.close()

print("Reading File")

file = open("ranking.txt", "r")

for line in file:
    print(line.strip())

file.close()
