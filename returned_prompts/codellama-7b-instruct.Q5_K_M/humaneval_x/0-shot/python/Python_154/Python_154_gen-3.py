
def cycpattern_check(a , b):
    return b in a or any(b[i:] + b[:i] in a for i in range(len(b)))
