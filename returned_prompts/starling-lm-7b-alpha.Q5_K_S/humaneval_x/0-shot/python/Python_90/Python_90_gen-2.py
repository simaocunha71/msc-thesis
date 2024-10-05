    # Initialize the minimum and second_minimum to positive infinity
    minimum = float('inf')
    second_minimum = float('inf')

    # Iterate over the list of integers
    for num in lst:
        # If the current number is smaller than the minimum,
        # then the current number is the new minimum
        if num < minimum:
            # Save the current number as the new minimum
            second_minimum = minimum
            # Save the current number as the new minimum
            minimum = num
        # If the current number is not smaller than the minimum but
        # it is smaller than the second minimum, then the current
        # number is the new second minimum
        elif num < second_minimum:
            # Save the current number as the second minimum
            second_minimum = num

    # Return the second minimum if the second minimum exists
    if second_minimum == float('inf'):
        # If there is no second minimum, then return None
        return None
    else:
        return second_minimum

# Test cases
print(next_smallest([1, 2, 3, 4, 5]))  # 2
print(next_smallest([5, 1, 4, 3, 2]))  # 2
print(next_smallest([]))  # None
print(next_smallest([1, 1]))  # None




























































































































































































