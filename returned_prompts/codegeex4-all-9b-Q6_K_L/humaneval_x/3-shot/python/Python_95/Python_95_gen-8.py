    if len(dict) == 0:
        return False

    first_key = list(dict.keys())[0]
    first_key_is_upper = first_key.isupper()

    for key in dict.keys():
        if key.isupper() != first_key_is_upper:
            return False

    return True

