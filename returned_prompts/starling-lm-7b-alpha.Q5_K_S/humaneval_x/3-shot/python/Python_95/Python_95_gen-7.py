    keys = dict.keys()
    if len(keys) == 0:
        return False

    first_key = keys[0]
    first_key_lower = first_key.lower()
    first_key_upper = first_key.upper()

    for key in keys:
        if key != first_key_lower and key != first_key_upper:
            return False

    return True


