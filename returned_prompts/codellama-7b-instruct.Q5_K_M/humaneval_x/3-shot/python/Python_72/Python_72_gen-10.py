    if w < len(q):
        return False
    elif len(q) == 1:
        return True
    else:
        for i in range(len(q)):
            if q[i] != q[-i-1]:
                return False
        return True


