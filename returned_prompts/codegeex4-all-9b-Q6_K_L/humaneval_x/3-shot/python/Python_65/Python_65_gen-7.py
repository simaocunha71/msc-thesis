    str_x = str(x)
    length = len(str_x)

    if shift > length:
        return str_x[::-1]

    return str_x[-shift:] + str_x[:-shift]