    x_n, x_d = map(int, x.split('/'))
    n_n, n_d = map(int, n.split('/'))

    return x_n * n_d == x_d * n_n


