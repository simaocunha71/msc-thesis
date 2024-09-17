def validate(n):
    d = {}
    for i in str(n):
        if i not in d:
            d[i] = 0
        d[i] += 1
    for i in d:
        if d[i] > int(i):
            return False
    return True