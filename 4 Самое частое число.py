a=input().split()
ind=0
c=0
for i in range(len(a)):
    if a.count(a[i])>c:
        c=a.count(a[i])
        ind=i
print(a[ind])

