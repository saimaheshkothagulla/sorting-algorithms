l=[int(x) for x in input().split(" ")]
c=0
for i in range(len(l)-1):
    for j in range(len(l)-i-1):
        if l[j]>l[j+1]:
            l[j],l[j+1]=l[j+1],l[j]
            c+=1
    if c==0:
        print(l)
        break

