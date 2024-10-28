def validate(n):
    n = str(n)
    for i in range(10):
        count = n.count(str(i))
        if count > i:
            return False
    return True