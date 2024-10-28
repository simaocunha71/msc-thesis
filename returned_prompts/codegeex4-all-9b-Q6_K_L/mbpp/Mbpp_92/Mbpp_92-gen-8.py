def is_undulating(n: int) -> bool:
    n = str(n)
    if len(n) < 3:
        return False
    for i in range(1, len(n)):
        if n[i] == n[i-1]:
            return False
    return True


