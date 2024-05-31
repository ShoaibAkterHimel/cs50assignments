time=input("What time is it?" )
x,y=time.split(":")
if "7" in x or "8" in x:
    print("breakfast time")
elif "12" or "13" in x:
    print("lunch time")

