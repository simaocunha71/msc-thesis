def is_undulating(n):
    n = str(n)
    if len(set(n)) == 1:
        return True
    return False