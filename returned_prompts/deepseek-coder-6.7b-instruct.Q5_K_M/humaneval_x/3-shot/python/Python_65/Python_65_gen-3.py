    x = str(x)
    shift = shift % len(x)
    return x[-shift:] + x[:-shift]


