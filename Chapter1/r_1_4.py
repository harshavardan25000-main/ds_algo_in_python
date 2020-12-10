def sum_suqares(n):
    return [i*i for i in range(1,n)]
if __name__=='__main__':
    print(sum(sum_suqares(5)))