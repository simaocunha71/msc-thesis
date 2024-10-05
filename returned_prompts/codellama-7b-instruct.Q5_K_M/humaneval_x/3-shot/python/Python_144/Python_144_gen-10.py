    x_n, x_d = x.split('/')
    n_n, n_d = n.split('/')
    return (int(x_n) * int(n_d)) % (int(x_d) * int(n_n)) == 0


