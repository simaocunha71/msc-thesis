    x = str(x)[::-1]  # convert to string and reverse
    shift = shift % len(x)  # adjust shift to be within the length of the string
    return x[shift:] + x[:shift]  # shift the string and return


