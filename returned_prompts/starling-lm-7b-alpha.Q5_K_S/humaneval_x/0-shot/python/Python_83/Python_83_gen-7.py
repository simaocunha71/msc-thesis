
    # Base cases
    if n == 0:
        return 0
    elif n == 1:
        return 2

    # Recursive step
    else:
        return 10 * starts_one_ends(n-1) + 2


