    if txt == '':
        return False

    last_char = txt[-1]
    return last_char.isalpha() and last_char not in ' ,.!?;:'


