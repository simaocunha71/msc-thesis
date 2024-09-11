def max_run_uppercase(s):
    """
    Finds maximum run of uppercase characters in the given string.

    Parameters:
        s (str): The string to be processed.

    Returns:
        int: The length of maximum run of uppercase characters.
    """
    result = 0
    max_length = 0
    for ch in s:
        if ch.isupper():
            result += 1
            if result > max_length:
                max_length = result
        else:
            result = 0
    return max_length