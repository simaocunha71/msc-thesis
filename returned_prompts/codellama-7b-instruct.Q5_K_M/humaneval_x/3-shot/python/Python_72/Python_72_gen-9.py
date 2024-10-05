    if sum(q) <= w:
        if q == q[::-1]:
            return True
        else:
            return False
    else:
        return False