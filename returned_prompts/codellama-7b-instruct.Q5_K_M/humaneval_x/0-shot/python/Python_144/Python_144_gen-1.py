
def simplify(x, n):
    a, b = x.split('/')
    c, d = n.split('/')
    if int(a) * int(d) == int(b) * int(c):
        return True
    else:
        return False