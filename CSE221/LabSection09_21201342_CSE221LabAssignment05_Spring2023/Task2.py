# Task 2

inp_file = open ('/content/drive/MyDrive/Colab Notebooks/CSE221/input2.txt', mode ='r')
data = inp_file.readlines()  # data = list
out_file= open ('/content/drive/MyDrive/Colab Notebooks/CSE221/output2.txt', mode ='w')

a={}
for i in range(1,int(data[0].split(' ')[1])+1):
    f=data[i].split(' ')
    if int(f[0]) not in a.keys():
        a[int(f[0])]=[int(f[1])]
    else:
        a[int(f[0])].append(int(f[1]))
q=[1]
final=[]
while q!=[]:
    if q[0] in a.keys():
        for i in a[q[0]]:
            q.append(i)
    if q[0] not in final:
        final.append(q[0])
    q.remove(q[0])
print(*final,file=out_file)