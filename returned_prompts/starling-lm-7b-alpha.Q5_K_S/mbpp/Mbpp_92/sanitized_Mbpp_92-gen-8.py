def is_undulating(n):
    n = str(n)
    if len(n) == 1:
        return False
    for i in range(1, len(n)):
        if n[i] != n[i - 1]:
            return True
    return False