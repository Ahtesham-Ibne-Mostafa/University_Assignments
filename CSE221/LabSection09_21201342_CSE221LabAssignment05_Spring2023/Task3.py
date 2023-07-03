# task 3

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input3.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output3.txt', mode ='w')

def dfs(graph, curr, visited):
    # mark the current node as visited
    visited[curr-1] = True
    
    print(curr, end=' ',file=out_file)
    
    # visit all the neighbors of the current node
    for neighbor in graph[curr]:
        if not visited[neighbor-1]:
            dfs(graph, neighbor, visited)

n, m = map(int, data[0].split(' '))
graph = [[] for _ in range(n+1)]

for i in range(1,m+1):
    u, v = map(int, data[i].split(' '))
    graph[u].append(v)
    graph[v].append(u)

visited = [False] * n
dfs(graph, 1, visited)
