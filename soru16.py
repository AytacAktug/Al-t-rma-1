def asal(x):
    for i in range(2,x):
        if x%i==0:
            return False
        return True
x=input("sayı gir:" )
x=int(x)
if asal(x)==True:
    print(x, "bir asal sayıdır.")
else:
    print(x, "bir asal sayı değildir.")