    if len(dict) == 0:
        return False

    first_key = list(dict.keys())[0]
    if not isinstance(first_key, str):
        return False

    if first_key.isupper():
        for key in dict.keys():
            if not isinstance(key, str) or not key.isupper():
                return False
    elif first_key.islower():
        for key in dict.keys():
            if not isinstance(key, str) or not key.islower():
                return False
    else:
        return False

    return True

