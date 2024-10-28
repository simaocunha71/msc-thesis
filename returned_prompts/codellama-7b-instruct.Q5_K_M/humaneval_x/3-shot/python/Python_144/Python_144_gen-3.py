    x_num, x_denom = x.split("/")
    n_num, n_denom = n.split("/")

    result = int(x_num) * int(n_num)
    if result % int(n_denom) == 0:
        return True

    return False


