    keys = dict.keys()
    if len(keys) == 0:
        return False
    for key in keys:
        if (key.isupper() and not all(char.isupper() for char in key)) or (key.islower() and not all(char.islower() for char in key)):
            return False
    return True


