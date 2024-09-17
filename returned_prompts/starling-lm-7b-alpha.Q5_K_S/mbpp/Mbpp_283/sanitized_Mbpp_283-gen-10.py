def validate(n):
    if(n < 0):
        return False
    n = str(n)
    d = {}
    for i in n:
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d:
        if d[i] > int(i):
            return False
    return True