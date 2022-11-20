
list = [(2,7),(1,6),(4,8),(5,9),(1,3)]
for i in range(len(list)):
    for j in range(len(list)):
        if list[i][1]<list[j][1]:
            list[i],list[j]=list[j],list[i]
print(list)






