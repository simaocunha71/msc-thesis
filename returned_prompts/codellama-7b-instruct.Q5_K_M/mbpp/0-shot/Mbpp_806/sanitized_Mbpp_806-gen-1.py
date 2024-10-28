def max_run_uppercase(s):
    """
    :param s: input string
    :return: maximum run of uppercase characters in the given string.
    """
    max_run = 0
    run = 0
    for c in s:
        if c.isupper():
            run += 1
        else:
            max_run = max(max_run, run)
            run = 0

    return max(max_run, run)