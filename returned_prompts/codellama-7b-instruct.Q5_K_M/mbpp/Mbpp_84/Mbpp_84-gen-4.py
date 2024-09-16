def sequence(n):
    # If n is 1, the answer is 1
    if n == 1:
        return 1
    # If n is 2, the answer is 1
    elif n == 2:
        return 1
    else:
        # If n is 3 or more, the answer is the number of 1s in the previous term plus the number of 2s in the previous term
        return sequence(n - sequence(n - 1)) + sequence(n - sequence(n - 2))
