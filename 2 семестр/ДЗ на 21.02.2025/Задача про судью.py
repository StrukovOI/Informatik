# Я немного изменил способ ввода данных, чтобы не разбивать входную строку на части для собрания нужного массива
n=int(input())  # Количество жителей
m=int(input())  # Количество массивов вида [a, b] (как в условии)
trust=[]

for i in range(m):
    k=list(map(int, input().split()))   # Массивы вводятся как два числа на одной строке, разделённые пробелом (например, '1 2')
    if k not in trust:
        trust.append(k)
    
def find(n, m, trust):
    a=[]
    for i in range(m):
        if trust[i][0] not in a:
            a.append(trust[i][0])
    if len(a)!=n-1:
        return -1
    
    for i in range(1, n+1):
        if i not in a:
            judge = i

    people={}
    for i in range(m):
        if people.get(trust[i][1], False) is False:
            people[trust[i][1]] = [trust[i][0]]
        else:
            people[trust[i][1]].append(trust[i][0])
    if sorted(people[judge])==sorted(a):
       return judge
    return -1


print(find(n, m, trust))