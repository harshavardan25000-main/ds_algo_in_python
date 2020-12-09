def factors(n):
    for i in range(1,n+1):
        yield i*i
if __name__=='__main__':
    result=factors(10)
    print(list(result))