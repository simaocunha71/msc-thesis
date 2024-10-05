
def cycpattern_check(a,b):
    a = a.lower()
    b = b.lower()
    for i in range(len(b)):
        if b[i:] in a:
            return True
    return False
