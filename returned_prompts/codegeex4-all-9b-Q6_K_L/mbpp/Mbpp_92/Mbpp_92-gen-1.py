def is_undulating(n):
    n = str(n)
    if len(n) < 3:
        return False
    for i in range(len(n)-1):
        if n[i] == n[i+1]:
            return False
    return True

