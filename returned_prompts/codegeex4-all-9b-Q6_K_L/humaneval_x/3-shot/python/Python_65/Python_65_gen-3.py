    str_x = str(x)
    len_x = len(str_x)

    if shift >= len_x:
        return str_x[::-1]

    return str_x[-shift:] + str_x[:-shift]