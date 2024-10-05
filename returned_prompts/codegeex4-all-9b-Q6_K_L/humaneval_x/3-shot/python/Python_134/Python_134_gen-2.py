    if len(txt) == 0:
        return False

    last_char = txt[-1]
    if not last_char.isalpha():
        return False

    if txt[-2] == ' ':
        return True

    return False

