    if not txt:
        return False

    last_char = txt[-1]
    if not last_char.isalpha():
        return False

    if txt.strip() == txt:
        return False

    return True

