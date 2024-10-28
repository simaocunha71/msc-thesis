def perfect_squares(n1,n2):
    l = []
    for i in range(n1,n2+1):
        if(i**0.5 == int(i**0.5)):
            l.append(i)
    return l