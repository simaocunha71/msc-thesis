    if not dict:
        return False

    keys = list(dict.keys())
    lower_keys = [k.lower() for k in keys]

    return keys == lower_keys or keys == [k.upper() for k in keys]


