    if a < 0:
        a = -a
    for i in range(1, a+1):
        if a == i**3:
            return True
    return False


