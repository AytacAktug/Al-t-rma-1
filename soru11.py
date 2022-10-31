X=[]
for a in range(124):
    for i in range(1,124):
        if 350%i==a and 125%i==a and 200%i==a:
            X.append(i)
            
print(max(X))
