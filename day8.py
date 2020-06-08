import random

if __name__ == "__main__":
    n=int(input())
    phoneBook = dict()

for i in range(n):
    friend = input()
    friend = friend.split()
    name = friend[0]
    phone = friend[1]
    phoneBook[name]=phone

for j in range(n):
    m = input()

    if(phoneBook.get(m)):
        print(m.strip(), phoneBook.get(m).strip(), sep="=")
    else:
        print("Not found")
