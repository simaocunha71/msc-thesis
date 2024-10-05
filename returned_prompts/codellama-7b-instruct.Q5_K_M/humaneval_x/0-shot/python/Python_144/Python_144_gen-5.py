
    if x[0] == '-' or n[0] == '-':
        return False

    x_n = int(x.split('/')[0])
    x_d = int(x.split('/')[1])

    n_n = int(n.split('/')[0])
    n_d = int(n.split('/')[1])

    if x_d % n_d == 0:
        return x_n % n_n == 0
    else:
        return False
