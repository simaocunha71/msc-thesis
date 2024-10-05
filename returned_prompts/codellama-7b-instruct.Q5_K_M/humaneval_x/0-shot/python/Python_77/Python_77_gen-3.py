
def iscube(a):
    for i in range(1, a+1):
        if pow(i, 3) == a:
            return True
    return False


