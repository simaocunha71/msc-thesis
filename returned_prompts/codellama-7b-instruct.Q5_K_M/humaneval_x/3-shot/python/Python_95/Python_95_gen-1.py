    if not dict:
        return False

    if all(isinstance(k, str) and k.islower() for k in dict):
        return True
    elif all(isinstance(k, str) and k.isupper() for k in dict):
        return True
    else:
        return False


