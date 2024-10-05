    if not dict:
        return False

    all_keys_lower = all(isinstance(key, str) and key.islower() for key in dict.keys())
    all_keys_upper = all(isinstance(key, str) and key.isupper() for key in dict.keys())

    return all_keys_lower or all_keys_upper


