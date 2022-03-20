import networkx as nx

n = int(input("Введите кол-во узлов"))
graph = nx.Graph()
for _ in range(n):
    graph.add_node(input())

print('Чтобы создать ребро введите узлы через пробел.Введите запятые чтобы прекратить создание ребер')
while True:
    a, b = input().split()
    if a == b == ',':
        break
    graph.add_edge(a, b)


def dfs(graph, start, visited=None):
    if visited is None:
        visited = set()
    visited.add(start)
    for next in set(graph[start]) - visited:
        print(set(graph[start]) - visited)
        dfs(graph, next, visited)
    return visited


dfs(graph, '0')
answer = 0
visited = set()
for _ in set(graph):
    if _ not in visited:
        a = (dfs(graph, _))
        visited = visited.union(a)
        answer += 1
print(answer)
