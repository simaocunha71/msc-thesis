def odd_num_sum(n):
    # Initialize result
    result = 0

    # Traverse through all odd numbers
    # from 1 to n and add their 4th power
    # to the result
    for i in range(1, 2*n + 1, 2):
        result += i**4

    return result