list=[]
maas= [10000,15000,20000,12000,13000]
for i in maas:
    if i < 15000:
        i = (i*20/100)+i
        list.append(i)
    else:
        list.append(i)
print(list)













