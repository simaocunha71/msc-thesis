    if not txt:
        return False
    last_char = txt[-1]
    return last_char.isalpha() and not last_char.isalnum()

