    if not dict:
        return False
    all_lowercase = all(isinstance(key, str) and key.islower() for key in dict)
    all_uppercase = all(isinstance(key, str) and key.isupper() for key in dict)
    return all_lowercase or all_uppercase


