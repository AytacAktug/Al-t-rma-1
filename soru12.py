def rakamtopla(x):
    if 1000<x<10000:
        x=str(x)
        a=(int(x[0])+int(x[1])+int(x[2])+int(x[3]))
        return a

for i in range(1000,10000):
    x=rakamtopla(i)
    if 2005-i==x:
        print(i)