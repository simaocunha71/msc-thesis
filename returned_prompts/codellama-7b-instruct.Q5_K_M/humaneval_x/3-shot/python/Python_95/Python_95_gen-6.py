    if len(dict) == 0:
        return False
    elif all(isinstance(key, str) and key.islower() for key in dict.keys()) or all(isinstance(key, str) and key.isupper() for key in dict.keys()):
        return True
    else:
        return False

