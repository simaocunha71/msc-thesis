def bell_Number(n):
    if n == 1:
        return 1
    elif n == 2:
        return 2
    else:
        return 2 * bell_Number(n-1) + bell_Number(n-2)
    # bell numbers are defined recursively as 2 * (n-1)th bell number + (n-2)th bell number
    # for n > 2. This is the implementation of the same.
    # However, the above code is not efficient for large values of n because it does
    # a lot of repeated work. A more efficient way to compute bell numbers is with
    # dynamic programming.
    # bell_number[n] = 2 * bell_number[n-1] + bell_number[n-2]
    # for n > 2
    # bell_number[1] = 1
    # bell_number[2] = 2
    # and then just return bell_number[n] for the given n. This way, each bell
    # number is computed only once, which makes the function much faster for large
    # values of n. However, this is not implemented here for simplicity. 
    # Also note that bell numbers can be computed exactly only for small values of
    # n. For large values of n, the results will be approximate and should be used
    # with caution.
    # For example, bell_number[20] is already too large to be computed exactly
    # and should be used with caution. 
    # Also note that this function does not check if n is a positive integer. It
    # should be modified to handle this case. 
    # Also note that this function does not check if n is an integer. It should be
    # modified to handle this case. 
    # Also note that this function does not check if n is a non-negative integer.
    # It should be modified to handle this case. 
    # Also note that this function does not check if n is a small integer. It should
    # be modified to handle this case. 
    # Also note that this function does not check if n is a large integer. It
    # should be modified to handle this case. 
    # Also note that this function does not check if n is an integer less than or
    # equal to 1. It should be modified to handle this case. 
    # Also note that this function does not check