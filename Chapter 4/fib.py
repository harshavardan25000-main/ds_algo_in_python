a,b=0,1
n=0
target=5
#0 1 1 2 3 5
def fib(a,b,n):
    if n==target:
        return
    print(a)
    a,b=b,a+b
    n+=1
    fib(a,b,n)
fib(a,b,n)


