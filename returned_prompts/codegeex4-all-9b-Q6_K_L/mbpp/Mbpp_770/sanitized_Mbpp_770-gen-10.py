def odd_num_sum(n):
    # Initialize the sum
    total_sum = 0

    # Iterate over the first n odd numbers
    for i in range(1, 2*n, 2):
        # Add the fourth power of the current odd number to the sum
        total_sum += i**4

    return total_sum