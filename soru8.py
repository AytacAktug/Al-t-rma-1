L=[]
for i in range(100,1000):
    x=str(i)
    if int(x[2])%2==0:
        if x[0]==x[1]==x[2] or x[0]==x[1] or x[0]==x[2] or x[1]==x[2] :
            L.append(x)
print(L,f"\n{len(L)} adet")