    x = str(x)
    shift %= len(x)

    if shift == 0:
        return x
    elif shift > 0:
        return x[-shift:] + x[:-shift]
    else:
        return x[:shift] + x[shift:]