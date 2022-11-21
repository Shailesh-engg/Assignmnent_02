len = int(input("enter a length of list: "))
lst=[]
for i in range(len):
    elements=(input("enter element with space sep: "))
    tup=tuple(int(item)for item in elements.split())
    lst.append(tup)
print(lst)

for i in range(len):
    for j in range(len):
        if lst[i][1]<lst[j][1]:
            lst[i],lst[j]=lst[j],lst[i]
print(lst)






