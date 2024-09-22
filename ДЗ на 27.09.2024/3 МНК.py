def MNK():
    x=input('Введите значения x разделяя их пробелами\n').split()
    y=input('Введите значения y разделяя их пробелами\n').split()
    if len(x)==len(y):
        for i in range(len(x)):
            x[i]=float(x[i])
        for i in range(len(y)):
            y[i]=float(y[i])
        
        a1=0
        a2=sum(x)*sum(y)
        a3=0
        a4=0
        b1=0
        b2=0

        for i in range(len(x)):
            a1+=x[i]*y[i]
            a3+=x[i]**2
            a4+=x[i]
            b1+=y[i]
        a1*=len(x)
        a3*=len(x)
        b2=a4
        a4**=2

        a=(a1-a2)/(a3-a4)
        b=(b1-a*b2)/len(x)

        return a, b
    else:
        return('Ошибка в введённых данных')
print(MNK())
