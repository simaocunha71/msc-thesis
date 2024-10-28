def is_undulating(n):
    str_n = str(n)
    if len(str_n) > 1 and len(set(str_n)) == 1:
        return True
    return False