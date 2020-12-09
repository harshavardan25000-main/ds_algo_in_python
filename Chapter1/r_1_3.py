def minmax(data):
    if len(data)==1:
        return (data[0],data[0])
    min_1,max_1=data[0],data[0]
    for i in range(1,len(data)):
        min_1=min(min_1,data[i])
        max_1=max(max_1,data[i])
    return (min_1,max_1)
data=[1]

if __name__=='__main__':
    result=minmax(data)
    print(result)