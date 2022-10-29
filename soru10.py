L=[]
for i in range(10000,100000):
    x=str(i)
    if x[0]==x[3] and x[1]==x[4]:
        L.append(x)
print(len(L))