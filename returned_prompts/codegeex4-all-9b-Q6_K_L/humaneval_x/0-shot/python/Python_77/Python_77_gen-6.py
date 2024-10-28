def iscube(a):
    if a <= 0:
        return True
    for i in range(1, int(a**0.5) + 1):
        if i**3 == a:
            return True
    return False