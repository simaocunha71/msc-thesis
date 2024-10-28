    x_str = str(x)[::-1]
    return x_str[shift % len(x_str):] + x_str[:shift % len(x_str)]


