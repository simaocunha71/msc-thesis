def validate(n):
    n=str(n)
    for i in n:
        if int(i) > 0 and n.count(i) > int(i):
            return False
    return True