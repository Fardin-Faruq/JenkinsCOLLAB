machines = [
    {"id":"M101","plant":"Chennai","hours":100,"down":10,"energy":500,"units":900,"cost":60000},
    {"id":"M102","plant":"Bangalore","hours":120,"down":20,"energy":700,"units":950,"cost":85000},
    {"id":"M103","plant":"Chennai","hours":90,"down":5,"energy":450,"units":850,"cost":50000}
]

for machine in machines:
    machine["efficiency"] = machine["units"] / (machine["hours"] - machine["down"])
    machine["unit_cost"] = machine["cost"] / machine["units"]

print("Machine Efficiency")
for machine in machines:
    print(machine["id"], round(machine["efficiency"],2))

print("\nProduction Cost Per Unit")
for machine in machines:
    print(machine["id"], round(machine["unit_cost"],2))

print("\nInefficient Machines")
for machine in machines:
    if machine["efficiency"] < 8:
        print(machine["id"])

highest = machines[0]

for machine in machines:
    if machine["cost"] > highest["cost"]:
        highest = machine

print("\nHighest Maintenance Cost")
print(highest["id"], highest["cost"])

plant_eff = {}

for machine in machines:
    if machine["plant"] in plant_eff:
        plant_eff[machine["plant"]] += machine["efficiency"]
    else:
        plant_eff[machine["plant"]] = machine["efficiency"]

print("\nPlant Wise Efficiency")
for plant in plant_eff:
    print(plant, round(plant_eff[plant],2))

print("\nMachines Requiring Preventive Maintenance")
for machine in machines:
    if machine["cost"] > 70000:
        print(machine["id"])

machines.sort(key=lambda machine: machine["efficiency"], reverse=True)

print("\nMachines Sorted By Efficiency")
for machine in machines:
    print(machine["id"], round(machine["efficiency"],2))

file = open("report.txt","w")

for machine in machines:
    file.write(machine["id"] + " " + str(round(machine["efficiency"],2)) + "\n")

file.close()

print("\nReading Report")

file = open("report.txt","r")

for line in file:
    print(line.strip())

file.close()
