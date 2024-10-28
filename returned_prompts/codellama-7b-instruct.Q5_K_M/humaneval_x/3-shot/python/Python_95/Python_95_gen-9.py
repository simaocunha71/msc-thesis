    if not dict:
        return False
    if all(isinstance(k, str) and k.islower() for k in dict.keys()):
        return True
    if all(isinstance(k, str) and k.isupper() for k in dict.keys()):
        return True
    return False


