for i in range(10,100):
    for x in range(10,100):
        y=str(x)+str(i)
        if int(y)==(i+x)*11:
            print(i,x)