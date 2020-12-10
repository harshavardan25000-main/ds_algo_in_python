def minmax(data):
    if not data:
        return None
    min_1,max_1=float('inf'),float('-inf')
    for i in data:
        if i<min_1:
            min_1=i
        if i>max_1:
            max_1=i
    return (min_1,max_1)
data=[1,2,3,4]

if __name__=='__main__':
    result=minmax(data)
    print(result)