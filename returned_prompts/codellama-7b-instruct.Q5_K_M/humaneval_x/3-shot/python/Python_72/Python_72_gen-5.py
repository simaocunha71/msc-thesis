    if w < max(q):
        return False
    if len(q) == 1:
        return True
    if q == q[::-1]:
        return True
    else:
        return False

