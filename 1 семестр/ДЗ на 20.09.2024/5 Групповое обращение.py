z=input().split()
c=0
z[1]='*'+z[1]
for i in range(len(z[1])//int(z[0])):
    print(z[1][c+int(z[0]):c:-1], end='')
    c+=int(z[0])