def asal(x):
    for i in range(2,x):
        if x%i==0:
            return False
        return True
    
for i in range(10000,100000):
    if asal(i)==True:
        print(i)
        
"""neden olmadığını anlamadım, range'i küçük yazınca doğru yapıyor büyüyünce yanlış."""