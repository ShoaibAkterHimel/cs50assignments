def main():
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    tip = dollars * percent
    print(f"Leave ${tip:.2f}\n")




def dollars_to_float(d):
    if  "$" in d:
        x,y=d.split("$")
    return float(y)


def percent_to_float(p):
    if "%" in p:
        x,y=p.split("%")
        i=float(x)
        i=i/100
        return (i)


main()

