l=[int(x) for x in input().split(" ")]
for i in range(len(l)):
    mini=i
    for j in range(i+1,len(l)):
        if l[j]<l[i]:
            mini=j
    if i!=mini:
        l[i],l[mini]=l[mini],l[i]
print(l)

