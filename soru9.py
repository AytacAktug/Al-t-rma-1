L=[]
for i in range(1,1000):
    x=str(i)
    if 9 < int(x) < 100:
        if int(x[0])+int(x[1])<9:
            L.append(x)
    elif int(x)> 99:
        if int(x[0])+int(x[1])+int(x[2]) < 9:
            L.append(x)
    else:
        L.append(x)
print(L,end=" ")
    
    
