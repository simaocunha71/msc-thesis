
def iscube(a):
    for x in range(1, a+1):
        if a == x**3:
            return True
    return False
