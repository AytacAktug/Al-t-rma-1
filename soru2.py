i=1
x=0
while i < 9999999:
    x+=1/i**2
    i+=1
    if i > 9999999:
        break
print(f"π sayısı yaklaşık olarak bu diziden {(x*6)**0.5} hesaplanmaktadır.")