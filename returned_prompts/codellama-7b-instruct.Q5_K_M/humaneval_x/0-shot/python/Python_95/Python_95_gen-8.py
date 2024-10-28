
    if not dict:
        return False
    return all(key.islower() for key in dict) or all(key.isupper() for key in dict)
