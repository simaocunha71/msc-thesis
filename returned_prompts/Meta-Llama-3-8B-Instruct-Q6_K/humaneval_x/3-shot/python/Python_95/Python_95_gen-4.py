    if not dict:
        return False

    if all(isinstance(key, str) and key.islower() for key in dict.keys()):
        return True
    elif all(isinstance(key, str) and key.isupper() for key in dict.keys()):
        return True
    else:
        return False


