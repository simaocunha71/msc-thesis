def sum(a,b):
    c = []
    for i in range(1,a+1):
        if i%a==0 and i%b==0:
            c.append(i)
    return sum(c)