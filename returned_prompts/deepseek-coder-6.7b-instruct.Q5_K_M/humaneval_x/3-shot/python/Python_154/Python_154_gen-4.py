    for i in range(len(b)):
        if b in a or b[::-1] in a:
            return True
        b = b[-1:] + b[:-1]
    return False


