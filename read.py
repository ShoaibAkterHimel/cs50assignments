import csv
lines=[]
with open("name.csv") as file:
    reader=csv.DictReader(file)
    for row in reader:
        dict={"name":row["name"], "home":row["home"]}
        lines.append(dict)


for i in sorted(lines, key=lambda lines: lines["name"]):
    print(f"{i["name"]} is in {i["home"]}")

