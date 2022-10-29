L=[]
for i in range(1000,10000):
    x=str(i)
    if x[0]>x[3]:
        L.append(x)
print(len(L))
