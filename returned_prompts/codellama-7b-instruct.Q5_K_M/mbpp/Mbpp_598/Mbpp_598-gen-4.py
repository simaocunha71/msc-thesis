def armstrong_number(n):
    s = str(n)
    return sum([int(i)**len(s) for i in s])==n


