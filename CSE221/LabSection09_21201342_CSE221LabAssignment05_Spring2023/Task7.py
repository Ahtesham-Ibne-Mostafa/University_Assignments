# Bonus Task 7

from collections import defaultdict

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input7.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output7.txt', mode ='w')

def dfs(node, visited, graph):
    visited[node] = True
    max_dist, max_node = 0, node
    for neighbor in graph[node]:
        if not visited[neighbor]:
            dist, farthest_node = dfs(neighbor, visited, graph)
            if dist + 1 > max_dist:
                max_dist = dist + 1
                max_node = farthest_node
    return max_dist, max_node

def find_max_distance(n, edges):
    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)
    visited = [False] * (n + 1)
    dist, node = dfs(1, visited, graph)
    visited = [False] * (n + 1)
    max_dist, _ = dfs(node, visited, graph)
    return (node, _)

n = int(data[0])
edges = []
for i in range(1,n):
    u, v = map(int, data[i].split())
    edges.append((u, v))

a, b = find_max_distance(n, edges)
print(a, b,file=out_file)
