def sum_squares_odd(n):
    return sum([i*i for i in range(1,n) if i%2==1])
print(sum_squares_odd(5))