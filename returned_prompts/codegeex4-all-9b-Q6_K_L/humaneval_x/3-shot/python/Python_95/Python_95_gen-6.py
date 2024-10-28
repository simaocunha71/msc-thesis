    if not dict:
        return False
    is_lower = all(key.islower() for key in dict.keys())
    is_upper = all(key.isupper() for key in dict.keys())
    return is_lower or is_upper

