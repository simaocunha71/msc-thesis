    str_x = str(x)[::-1]
    shift = shift % len(str_x)
    return str_x[shift:] + str_x[:shift][::-1] if shift > len(str_x) // 2 else str_x[shift:] + str_x[:shift]  # Python 3.8+


