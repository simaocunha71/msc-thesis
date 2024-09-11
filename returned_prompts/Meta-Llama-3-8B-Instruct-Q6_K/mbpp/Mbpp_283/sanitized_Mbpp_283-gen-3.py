def validate(n):
    n = str(n)
    for i in set(n):
        if n.count(i) > int(i):
            return False
    return True