def sum_suqares(n):
    for i in range(1,n):
        yield i*i
if __name__=='__main__':
    print(sum(sum_suqares(5)))