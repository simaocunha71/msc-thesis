    if not dict:
        return False
    for key in dict:
        if not isinstance(key, str):
            return False
        if key.islower() != all(k.islower() for k in dict):
            return False
        if key.isupper() != all(k.isupper() for k in dict):
            return False
    return True

