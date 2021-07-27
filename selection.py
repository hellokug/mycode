arr =[3,1,2,5,6,9,4,7,8]
len = len(arr)
i=0
while i < len:
    minpos=i
    j=i+1
    while j < len:
        if arr[minpos]>arr[j]:
            minpos = j
        j+=1
    temp=arr[minpos]
    arr[minpos]=arr[i]
    arr[i]=temp
    i+=1
    print(arr)
    