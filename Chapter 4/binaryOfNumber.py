def bin(n):
    if n < 2:
        print(int(n%2),end="")
        return
    bin(n/2)
    print(int(n%2),end="")
bin(5)


