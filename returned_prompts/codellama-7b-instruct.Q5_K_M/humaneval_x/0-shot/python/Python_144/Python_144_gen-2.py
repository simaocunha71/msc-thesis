
def simplify(x, n):
    x = x.split('/')
    n = n.split('/')
    if int(x[0]) * int(n[1]) == int(n[0]) * int(x[1]):
        return True
    else:
        return False
