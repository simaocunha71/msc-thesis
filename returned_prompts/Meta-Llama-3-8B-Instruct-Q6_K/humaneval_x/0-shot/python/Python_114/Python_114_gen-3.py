    # Initialize the minimum sum and the current sum to positive infinity
    min_sum = float('inf')
    current_sum = 0

    # Iterate over the array
    for num in nums:
        # Add the current number to the current sum
        current_sum += num

        # If the current sum is less than the minimum sum, update the minimum sum
        if current_sum < min_sum:
            min_sum = current_sum

        # If the current sum is greater than 0, reset it to 0
        if current_sum > 0:
            current_sum = 0

    # Return the minimum sum
    return min_sum

