    if not dict:
        return False
    keys = dict.keys()
    if all(key.islower() for key in keys):
        return True
    if all(key.isupper() for key in keys):
        return True
    return False


