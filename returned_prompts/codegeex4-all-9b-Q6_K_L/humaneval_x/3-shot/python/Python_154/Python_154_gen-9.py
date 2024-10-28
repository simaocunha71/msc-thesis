    for i in range(len(b)):
        if b in a or b[i:] + b[:i] in a:
            return True
    return False

