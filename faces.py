def convert(str):
    list=[]
    if ":)" and ":(" in str:
        list.append(str.replace(":)", "🙂"))
        list.append(list[0].replace(":(", "🙁"))
        return list[1]
    if ":)" in str:
        list.append(str.replace(":)", "🙂"))
        return list[0]
    if ":(" in str:
        list.append(str.replace(":(", "🙁"))
        return list[0]






def main():
    x=input()
    print(convert(x))
main()
