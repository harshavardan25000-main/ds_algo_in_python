def binary_search(data,start,end):

    if start>=end:
        result.append(None)
        return
    mid = (start + end) // 2
    if data[mid]==target:
        result.append(mid)
        return
    elif data[mid]>target:
        binary_search(data,start,mid)
    else:
        binary_search(data,mid+1,end)


data=[1,2,3,4,5,6,7,8]
target=7
result=[]
binary_search(data,0,len(data))
print(result[0])
