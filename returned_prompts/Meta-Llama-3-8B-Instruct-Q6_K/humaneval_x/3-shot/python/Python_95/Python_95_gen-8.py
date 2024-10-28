    if not dict:
        return False

    keys = list(dict.keys())
    if all(isinstance(k, str) and k.islower() for k in keys):
        return True
    elif all(isinstance(k, str) and k.isupper() for k in keys):
        return True
    else:
        return False


