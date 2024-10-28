    if b in a:
        return True
    else:
        for i in range(len(b)):
            if b[i:] == b[:len(b)-i] and b[i:] in a:
                return True
        return False
