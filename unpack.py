def main():
    yell("This","is", "Cs50")

def yell(*words):
    uppercased=map(str.upper, words)
    print(*uppercased)
main()

