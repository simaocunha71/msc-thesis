    x_str = str(x)
    shift = shift % len(x_str)

    if shift == 0:
        return x_str
    elif shift > len(x_str):
        return x_str[::-1]
    else:
        return x_str[shift:] + x_str[:shift]  # Python slice syntax


