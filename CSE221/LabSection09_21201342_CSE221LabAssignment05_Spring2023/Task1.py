# Task 1 a

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input1a.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output1a.txt', mode ='w')
a=[]
for i in range(int(data[0].split(' ')[0])+1):
    b=[0]*(int(data[0].split(' ')[0])+1)
    a.append(b)
for i in range(1,int(data[0].split(' ')[1])+1):
    f=list(map(int, data[i].strip().split(' ')))
    a[f[0]][f[1]]=f[2]
for i in a:
    print(*i,file=out_file)
    
    
    
    
    
# Task 1 b

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input1b.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output1b.txt', mode ='w')
a={}
for i in range(1,int(data[0].split(' ')[1])+1):
    f=data[i].split(' ')
    if int(f[0]) not in a.keys():
        a[int(f[0])]=[(int(f[1]),int(f[2]))]
    else:
        a[int(f[0])].append((int(f[1]),int(f[2])))
for i in range(int(data[0].split(' ')[1])):
    if i not in a.keys():
        print(i,':',file=out_file)
    else:
        print(i,':',*a[i],file=out_file)