l=list(map(int,input().split(" ")))
for i in range(1,len(l)):
    temp=l[i]
    j=i-1
    while(l[j]>temp and j>=0):
        l[j+1]=l[j]
        j-=1
    l[j+1]=temp
print(l)

