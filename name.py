name=input("what's your name and house?")
with open("name.csv","a") as file:
    file.write(f"{name}\n")
