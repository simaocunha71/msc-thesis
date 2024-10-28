    if not dict:
        return False

    lower_case_keys = [k for k in dict.keys() if isinstance(k, str) and k.islower()]
    upper_case_keys = [k for k in dict.keys() if isinstance(k, str) and k.isupper()]

    return len(lower_case_keys) == len(dict) or len(upper_case_keys) == len(dict)


