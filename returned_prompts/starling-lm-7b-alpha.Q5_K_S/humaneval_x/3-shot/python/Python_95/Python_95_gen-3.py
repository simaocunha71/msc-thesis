    keys = dict.keys()
    if not keys:
        return False

    for key in keys:
        if key.lower() != key or key.upper() != key:
            return False

    return True


