def validate(n):
    n_str = str(n)
    for i in range(10):
        count = n_str.count(str(i))
        if count > i:
            return False
    return True