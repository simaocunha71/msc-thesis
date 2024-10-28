    if q==[]:
        return False
    if sum(q)>w:
        return False
    if sum(q)==w:
        return True
    if sum(q)<w:
        if q==q[::-1]:
            return True
        else:
            return False


