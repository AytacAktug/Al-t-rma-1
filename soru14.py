F=[]
for x in range(1,1000):
    for i in range(1,1000):
        if x*i==121212:
            f=abs(x-i)
            F.append(f)
            if (x-i)==min(F):
                print(x,i)