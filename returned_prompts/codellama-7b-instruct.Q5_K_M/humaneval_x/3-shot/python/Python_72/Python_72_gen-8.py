    if q == []:
        return False
    elif len(q) == 1:
        return True
    elif sum(q) <= w and q == q[::-1]:
        return True
    else:
        return False


