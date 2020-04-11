l=list(map(int,input().split(" ")))
h=5
while(h>=1):
    for i in range(h,len(l)):
        temp=l[i]
        j=i-h
        while(l[j]>temp and j>=0):
            l[j+h]=l[j]
            j-=h
        l[j+h]=temp
    h-=2
print(l)

