k=int(input("Введите количество людей:\n"))
n=int(input("Введите количество пар dislikes:\n"))
graph={}

for i in range(n):
    dis=list(map(int, input().split()))
    if graph.get(dis[0], False) is False:
        graph[dis[0]] = [dis[1]]
    else:
        graph[dis[0]].append(dis[1])
for i in range(1, k+1):
    if graph.get(i, False) is False:
        graph[i] = []


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