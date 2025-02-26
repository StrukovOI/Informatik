k=int(input("Введите количество людей:\n"))
n=input("Введите массив dislikes:\n").split(',')
graph={}
m=[]

for i in n:
    el=''
    for j in i:
        if j.isdigit():
            el=el+j
    m.append(int(el))

for i in range(len(m)//2):
    if graph.get(m[i*2], False) is False:
        graph[m[i*2]] = [m[i*2+1]]
    else:
        graph[m[i*2]].append(m[i*2+1])
for i in range(1, k+1):
    if graph.get(i, False) is False:
        graph[i] = [i]

def is_bipartite_dfs(graph, node, colors=None, color=0):
    if colors is None:
        colors = {}  # Словарь для хранения цветов вершин
    
    if node in colors:
        return colors[node] == color  # Проверяем, что вершина уже окрашена правильно
    
    colors[node] = color  # Красим текущую вершину в текущий цвет
    
    for neighbor in graph[node]:
        # Рекурсивно проверяем соседей, окрашивая их в противоположный цвет
        if not is_bipartite_dfs(graph, neighbor, colors, 1 - color):
            return False
    
    return True

def check_bipartite(graph):
    colors = {}  # Словарь для хранения информации о цветах вершин
    first=[]
    second=[]  # Словарь для хранения информации о цветах вершин
    for node in graph:
        if node not in colors:  # Проверяем каждую компоненту связности
            if not is_bipartite_dfs(graph, node, colors):
                return False, first, second  # Если хоть одна компонента не двудольная, возвращаем False

    for i in colors:
        if colors[i]==0:
            first.append(i)
        else:
            second.append(i)
    return True, first, second

ans, f, s=check_bipartite(graph)
if ans==False:
    print('Людей поделить на две группы невозможно')
else:
    f, s=map(str, f), map(str, s)
    print(f"Людей можно разделить на две группы:\nЛюди в первой группе: {' '.join(f)}\nЛюди во второй группе: {' '.join(s)}")