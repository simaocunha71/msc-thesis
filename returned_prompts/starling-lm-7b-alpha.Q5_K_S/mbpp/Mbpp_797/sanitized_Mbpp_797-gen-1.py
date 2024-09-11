def sum_in_range(l, r):
    # Initialize result
    result = 0
    # Traverse through all numbers in the range r to l
    for i in range(l, r + 1):
        # If current number is odd, add it to result
        if i % 2 != 0:
            result += i
    return result