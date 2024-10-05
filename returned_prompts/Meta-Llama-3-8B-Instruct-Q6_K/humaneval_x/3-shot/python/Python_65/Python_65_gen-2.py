    str_x = str(x)
    shift = shift % len(str_x)
    return str_x[-shift:] + str_x[:-shift] if shift > 0 else str_x[shift:] + str_x[:shift] if shift < 0 else str_x


