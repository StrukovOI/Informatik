city=input().split()
graph={}

for i in city:
    graph[i]=[]
    for j in city:
        if i[-1]==j[0]:
            graph[i].append(j)

def topological_sort_dfs(graph):
    visited = set()
    stack = []

    def dfs(node):
        if node in visited:
            return
        visited.add(node)
        
        for neighbor in graph[node]:
            dfs(neighbor)
        
        stack.append(node)

    for node in graph:
        if node not in visited:
            dfs(node)

    for i in range(len(stack)-1):
        if stack[i][0]!=stack[i+1][-1]:
            return False
    return True

print(topological_sort_dfs(graph))