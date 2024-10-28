    str_x = str(x)
    shift %= len(str_x)
    return str_x[-shift:] + str_x[:-shift]