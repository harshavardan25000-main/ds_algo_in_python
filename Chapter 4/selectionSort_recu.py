input=[-7,5,0,13,41,2,1]
start=0
end=len(input)
index=0
def minfind(input,start,end):
    minele = float('inf')
    for i in range(start,end):
        if input[i]<minele:
            minele=input[i]
            index=i
    return index

def selSort(input,start,end):
    if start>=end:
        return
    min_index=minfind(input,start,end)
    input[start],input[min_index]=input[min_index],input[start]
    selSort(input,start+1,end)

selSort(input,start,end)
print(input)