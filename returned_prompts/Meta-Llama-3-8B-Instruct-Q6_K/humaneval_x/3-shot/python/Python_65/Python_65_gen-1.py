    num_str = str(x)
    shift = shift % len(num_str)
    return num_str[-shift:] + num_str[:-shift] if shift > 0 else num_str


