def validate(n):
    n_str = str(n)
    for i in n_str:
        if n_str.count(i) > int(i):
            return False
    return True