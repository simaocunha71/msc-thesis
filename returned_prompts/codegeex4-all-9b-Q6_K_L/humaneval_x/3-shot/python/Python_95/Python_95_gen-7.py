    if not dict:
        return False

    first_key = list(dict.keys())[0]
    if not isinstance(first_key, str):
        return False

    all_lower = first_key.islower()
    all_upper = first_key.isupper()

    for key in dict.keys():
        if not isinstance(key, str):
            return False

        if key.islower() != all_lower or key.isupper() != all_upper:
            return False

    return True

