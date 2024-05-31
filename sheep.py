def main():
    n=int(input("number of sheep: "))
    for s in sheep(n):
        print(s)
def sheep(n):
    flock=[]
    for i in range(n):
        flock.append("🐑"*i)
    return flock
main()
