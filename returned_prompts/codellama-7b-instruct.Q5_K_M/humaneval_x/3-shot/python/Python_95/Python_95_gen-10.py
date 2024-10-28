    if len(dict) == 0:
        return False

    all_keys_are_strings = True
    all_keys_are_uppercase = True
    all_keys_are_lowercase = True

    for key in dict.keys():
        if not isinstance(key, str):
            all_keys_are_strings = False

        if key != key.lower() and key != key.upper():
            all_keys_are_uppercase = False
            all_keys_are_lowercase = False

        if all_keys_are_uppercase:
            if not key == key.upper():
                all_keys_are_uppercase = False

        if all_keys_are_lowercase:
            if not key == key.lower():
                all_keys_are_lowercase = False

    return all_keys_are_strings and (all_keys_are_uppercase or all_keys_are_lowercase)


