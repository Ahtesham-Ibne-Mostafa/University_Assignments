# task 4

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input4.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output4.txt', mode ='w')

def has_cycle(graph, curr, visited, stack):
    visited[curr-1] = True
    stack[curr-1] = True
    
    for neighbor in graph[curr]:
        if not visited[neighbor-1]:
            if has_cycle(graph, neighbor, visited, stack):
                return True
        elif stack[neighbor-1]:
            return True
    
    stack[curr-1] = False
    return False

n, m = map(int, data[0].split(' '))
graph = [[] for _ in range(n+1)]

for i in range(1,m+1):
    u, v = map(int, data[i].split(' '))
    graph[u].append(v)

visited = [False] * n
stack = [False] * n

for i in range(1, n+1):
    if not visited[i-1]:
        if has_cycle(graph, i, visited, stack):
            print("YES",file=out_file)
            break
else:
    print("NO",file=out_file)
