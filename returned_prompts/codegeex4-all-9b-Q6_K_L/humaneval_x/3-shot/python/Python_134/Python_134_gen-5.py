    if txt == '':
        return False
    else:
        last_char = txt[-1]
        if last_char.isalpha() and not last_char.isalnum():
            return True
        else:
            return False

