def funktion ():
    a=int(input('Введите число, которое необходимо разложить на простые множители\n'))
    z=[]
    s = f'{a} ='
    while a!=1:
        for i in range(2, a+1):
            if a%i==0:
                z.append(i)
                a=a//i
                break
    for i in range(len(z)):
        s = f'{s} {z[i]} *'
    return s[:-1]
print(funktion())
