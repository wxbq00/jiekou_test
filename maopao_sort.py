arr=[5,9,34,3,24,12,23,2]
print('未排序前的元祖',arr)
for i in range(1,len(arr)):
    for j in range(0,len(arr)-i):
        if arr[j]>arr[j+1]:
            arr[j],arr[j+1]=arr[j+1],arr[j]
    print('第'+str(i)+'次排序',arr)
print('升序后的元祖',arr)