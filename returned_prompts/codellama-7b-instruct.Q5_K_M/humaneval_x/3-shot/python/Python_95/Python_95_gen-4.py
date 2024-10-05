    if not dict:
        return False

    keys = list(dict.keys())
    first_key = keys[0]

    if not isinstance(first_key, str):
        return False

    if not all(isinstance(k, str) for k in keys):
        return False

    if all(k.islower() for k in keys):
        return True

    if all(k.isupper() for k in keys):
        return True

    return False


