    if x < base:
        return str(x)

    return change_base(x // base, base) + str(x % base)


