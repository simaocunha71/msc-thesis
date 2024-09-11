def validate(n):
    n = str(n)
    for i in n:
        if int(i) == 0:
            continue
        if int(i) < n.count(i):
            return False
    return True