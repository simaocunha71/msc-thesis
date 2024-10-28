def is_undulating(n):
    n_str = str(n)
    for i in range(1, len(n_str)):
        if n_str[i] == n_str[i-1]:
            return False
    return True