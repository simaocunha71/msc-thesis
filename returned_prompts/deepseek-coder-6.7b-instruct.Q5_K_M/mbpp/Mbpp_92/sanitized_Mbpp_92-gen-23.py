def is_undulating(n):
    n = str(n)
    for i in range(len(n) - 2):
        if n[i] == n[i + 1] or n[i + 1] != n[i + 2]:
            return False
    return True