def is_lower(input_str):
    if isinstance(input_str, str):
        return input_str.lower()
    else:
        raise TypeError("Input must be a string")