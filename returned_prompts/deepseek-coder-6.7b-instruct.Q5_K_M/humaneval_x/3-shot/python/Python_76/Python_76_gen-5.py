    if n==1: return True
    while x > 1:
        x /= n
        if x==int(x): return True
    return False


