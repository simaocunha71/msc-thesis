    if len(txt) == 0:
        return False

    last_char = txt[-1]
    return last_char.isalpha() and not last_char.isalnum()

