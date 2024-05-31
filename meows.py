def meow(n):
    return "meow\n" *n

number=int(input("number: "))
meows=meow(number)
print(meows, end="")
