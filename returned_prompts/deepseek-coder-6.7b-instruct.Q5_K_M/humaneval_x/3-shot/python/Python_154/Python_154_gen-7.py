    for _ in range(len(b)):
        if b in a:
            return True
        b = b[-1:] + b[:-1]

    return False


