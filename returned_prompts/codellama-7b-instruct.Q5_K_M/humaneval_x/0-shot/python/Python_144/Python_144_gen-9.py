
def simplify(x, n):
    x_n, x_d = x.split('/')
    n_n, n_d = n.split('/')
    if int(x_n) * int(n_d) == int(x_d) * int(n_n):
        return True
    else:
        return False
