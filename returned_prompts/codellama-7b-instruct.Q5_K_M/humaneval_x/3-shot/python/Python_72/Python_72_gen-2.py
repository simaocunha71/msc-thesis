    if q == []:
        return False
    elif sum(q) <= w and q == q[::-1]:
        return True
    else:
        return False


