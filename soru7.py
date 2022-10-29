L=[]
for i in range(100,1000):
    x=str(i)
    if int(x[0])+int(x[1])==int(x[2]):
        L.append(x)
print((L))
