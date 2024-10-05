    if len(dict) == 0:
        return False

    first_key = list(dict.keys())[0]
    first_key_is_lower = first_key.islower()
    first_key_is_upper = first_key.isupper()

    for key in dict.keys():
        if first_key_is_lower and not key.islower():
            return False
        if first_key_is_upper and not key.isupper():
            return False

    return True

