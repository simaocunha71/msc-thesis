    if not dict:
        return False

    lower_case_keys = [k for k in dict if k.islower()]
    upper_case_keys = [k for k in dict if k.isupper()]

    if not lower_case_keys and not upper_case_keys:
        return False

    if lower_case_keys and upper_case_keys:
        return False

    return True


