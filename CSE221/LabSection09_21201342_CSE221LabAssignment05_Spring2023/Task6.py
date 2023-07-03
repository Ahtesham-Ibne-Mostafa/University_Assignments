# Task 6

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input6.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output6.txt', mode ='w')

R, C = map(int, data[0].split(' '))

grid = []
for i in range(1,R+1):
    row = data[i].strip()
    grid.append(row)

max_diamonds = 0
for r in range(R):
    for c in range(C):
        if grid[r][c] != '#':
            diamonds = 0
            stack = [(r, c)]
            while stack:
                x, y = stack.pop()
                if grid[x][y] == 'D':
                    diamonds += 1
                grid[x] = grid[x][:y] + '#' + grid[x][y+1:]
                if x > 0 and grid[x-1][y] != '#':
                    stack.append((x-1, y))
                if x < R-1 and grid[x+1][y] != '#':
                    stack.append((x+1, y))
                if y > 0 and grid[x][y-1] != '#':
                    stack.append((x, y-1))
                if y < C-1 and grid[x][y+1] != '#':
                    stack.append((x, y+1))
            max_diamonds = max(max_diamonds, diamonds)

print(max_diamonds,file=out_file)