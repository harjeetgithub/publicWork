def mean(arr):
    sum=0
    for x in arr:
        sum+=x
    return(sum/len(arr))


def sd(arr):
    arr1=[]
    y=mean(arr)
    for x in range(len(arr)):
        t=(arr[x]-y)
        arr1.append(t**2)
    arr1=(sum(arr1)**(1/2))
    print("standard diviation is",arr1/len(arr),"\nvariance is",arr1/len(arr)**2)


arr=[10,7,9,11,15,12,13,11,9,10]
print("mean is",mean(arr))
sd(arr)
