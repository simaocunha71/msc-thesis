
def iscube(a):
    if a < 0:
        return iscube(-a)
    for i in range(1, int(a ** 0.33) + 1):
        if a == i ** 3:
            return True
    return False

