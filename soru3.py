def faktöriyel(x):
    i=1
    if x==0:
        i=1
    else:
        for a in range(1,x+1):
            i*=a
    return i

e=0
x=0
while x<999:
    a=1/faktöriyel(x)
    e+=a
    x+=1
    if x>999:
        break
print(f"e sayısı yaklaşık olarak {e}'dir.")