    for i in range(len(b)):
        if b[i:] + b[:i] in a:
            return True
    return False

