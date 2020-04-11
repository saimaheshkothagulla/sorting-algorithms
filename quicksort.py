a=[int(x) for x in input().split(" ")]
n=len(a)
def qsort(a,low,high):
    if low>=high:
        return
    p=partition(a,low,high)
    qsort(a,low,p-1)
    qsort(a,p+1,high)
def partition(a,low,high):
    i=low+1
    j=high
    pivot=a[low]
    while(i<=j):
        while(a[i]<pivot and i<high):
            i+=1
        while(a[j]>pivot):
            j-=1
        if i<j:
            temp=a[i]
            a[i]=a[j]
            a[j]=temp
            i+=1
            j-=1
        else:
            break
    a[low]=a[j]
    a[j]=pivot
    return j
qsort(a,0,n-1)
print(a)