dict={}
len = int(input("enter length of alphabets: "))#26

for i in range(len):
    alphabets = input("enter the alpha: ")
    for i in alphabets:
        asc = ord(i)
        key = i
        value = asc
        dict[key] = value
print(dict)
