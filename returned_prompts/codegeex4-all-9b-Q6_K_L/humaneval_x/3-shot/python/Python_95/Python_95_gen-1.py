    if not dict:
        return False

    first_key = list(dict.keys())[0]
    if not isinstance(first_key, str):
        return False

    is_lower = first_key.islower()
    is_upper = first_key.isupper()

    for key in dict.keys():
        if not isinstance(key, str):
            return False
        if is_lower and not key.islower():
            return False
        if is_upper and not key.isupper():
            return False

    return True