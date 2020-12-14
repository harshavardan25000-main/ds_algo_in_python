input=[-7,5,0,13,41,2,1]
sorted_array=[]

while len(input)>=1:
    min_element = float('inf')
    for i in range(len(input)):
        min_element=min(min_element,input[i])
    sorted_array.append(min_element)
    input.remove(min_element)
print(sorted_array)


