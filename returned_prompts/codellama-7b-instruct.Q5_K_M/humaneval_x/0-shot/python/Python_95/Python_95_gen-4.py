
    if len(dict) == 0:
        return False

    if all(isinstance(k, str) and k.islower() for k in dict.keys()) or all(isinstance(k, str) and k.isupper() for k in dict.keys()):
        return True
    else:
        return False
