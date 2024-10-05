    all_keys_cap = all(k.isupper() for k in dict.keys())
    all_keys_lower = all(k.islower() for k in dict.keys())

    if all_keys_cap or all_keys_lower:
        return True
    else:
        return False


