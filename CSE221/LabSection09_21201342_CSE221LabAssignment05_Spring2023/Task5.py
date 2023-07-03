# Task 5

import heapq

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input5.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output5.txt', mode ='w')

def dijkstra(graph, start, end):
    n = len(graph)
    dist = [float('inf')] * n
    parent = [-1] * n
    dist[start] = 0
    q = [(0, start)]

    while q:
        d, u = heapq.heappop(q)
        if d != dist[u]:
            continue
        if u == end:
            break
        for v in graph[u]:
            if dist[u] + 1 < dist[v]:
                dist[v] = dist[u] + 1
                parent[v] = u
                heapq.heappush(q, (dist[v], v))

    path = [end]
    while path[-1] != start:
        path.append(parent[path[-1]])
    path.reverse()
    return dist[end], path

n, m, d = map(int, data[0].split(' '))
graph = [[] for _ in range(n)]
for i in range(1,m):
    u, v = map(int, data[i].split(' '))
    graph[u-1].append(v-1)
    graph[v-1].append(u-1)

dist, path = dijkstra(graph, 0, d-1)
print('Time:',dist,file=out_file)
print('Shortest Path:',' '.join(str(x+1) for x in path),file=out_file)