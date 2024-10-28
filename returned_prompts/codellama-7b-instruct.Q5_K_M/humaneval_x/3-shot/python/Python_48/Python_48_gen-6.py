    text = text.lower()

    if len(text) == 0:
        return True

    for idx, c in enumerate(text):
        if text[idx] != text[-idx-1]:
            return False

    return True


