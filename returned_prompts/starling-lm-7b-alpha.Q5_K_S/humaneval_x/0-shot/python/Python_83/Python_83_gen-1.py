
    # If n is 1, return 2 because the numbers can be 1 or 10
    if n == 1:
        return 2

    # The first digit can't be zero, so there are n-1 possibilities
    # for the first digit, and 10 possibilities for the remaining n-1 digits
    if n > 1:
        return (n-1) * 10 ** (n-1)

    # The last digit can't be zero, so there are 9 possibilities for the
    # last digit, and 10 ** (n-1) possibilities for the remaining n-1 digits
    return 9 * 10 ** (n-1)


