from collections import defaultdict

def max_bipartite_nodes(graph):
    visited = defaultdict(bool)
    colors = defaultdict(lambda: -1)

    def dfs(node, color):
        visited[node] = True
        colors[node] = color

        max_nodes = 1
        for neighbor in graph[node]:
            if not visited[neighbor]:
                max_nodes += dfs(neighbor, 1 - color)
            elif colors[node] == colors[neighbor]:
                max_nodes = 0

        return max_nodes

    max_nodes = 0
    for node in graph:
        if not visited[node]:
            max_nodes += dfs(node, 0)

    return max_nodes


t = int(input())

for case in range(1, t+1):
    n = int(input())
    edges = [tuple(map(int, input().split())) for i in range(n)]

    graph = defaultdict(list)
    for u, v in edges:
        graph[u].append(v)
        graph[v].append(u)

    max_nodes = max_bipartite_nodes(graph)

    print("Case {}: {}".format(case, max_nodes))

