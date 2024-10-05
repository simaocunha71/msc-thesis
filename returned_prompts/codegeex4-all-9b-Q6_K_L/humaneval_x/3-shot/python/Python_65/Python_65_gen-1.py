    if shift > len(str(x)):
        return str(x)[::-1]
    else:
        return str(x)[-shift:] + str(x)[:-shift]