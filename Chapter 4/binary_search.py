def binary_search(data,start,end):

    if start>=end:
        return None
    mid = (start + end) // 2
    if data[mid]==target:
        return mid
    elif data[mid]>target:
        return binary_search(data,start,mid)
    else:
        return binary_search(data,mid+1,end)

data=[1,2,3,4,5,6,7,8]
target=7
print(binary_search(data,0,len(data)))

