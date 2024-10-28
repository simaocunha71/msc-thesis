    last_char = txt[-1]

    if last_char.isalpha() and last_char not in ' ':
        return True
    else:
        return False


