
def iscube(a):
    for x in range(1, a+1):
        if x**3 == a:
            return True
    return False
