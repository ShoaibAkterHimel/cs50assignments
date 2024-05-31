x=input("expression: ")
if "+" in x:
    x,z=x.split("+")
    x=int(x)
    z=int(z)
    sum=x+z
    print(float(sum))
elif "-" in x:
    x,z=x.split("-")
    x=int(x)
    z=int(z)
    sub=x-z
    print(float(sub))
elif "*" in x:
    x,z=x.split("*")
    x=int(x)
    z=int(z)
    multi=x*z
    print(float(multi))
elif "/" in x:
    x,z=x.split("/")
    x=int(x)
    z=int(z)
    div=x/z
    print(float(div))
