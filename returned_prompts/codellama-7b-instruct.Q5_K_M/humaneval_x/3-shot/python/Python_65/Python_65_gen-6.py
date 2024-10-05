    s = str(x)

    if len(s) <= shift:
        return s[::-1]

    return s[shift:] + s[:shift]


