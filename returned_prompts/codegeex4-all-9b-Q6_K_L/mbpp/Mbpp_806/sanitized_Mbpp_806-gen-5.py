def max_run_uppercase(s: str) -> int:
    """
    Finds the maximum run of uppercase characters in the given string.
    :param s: Input string
    :return: Length of maximum run of uppercase characters
    """
    max_run = 0
    current_run = 0
    for char in s:
        if char.isupper():
            current_run += 1
            max_run = max(max_run, current_run)
        else:
            current_run = 0
    return max_run