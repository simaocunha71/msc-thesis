    x = str(x)
    shift %= len(x)
    return x[-shift:] + x[:-shift]


