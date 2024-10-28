def max_sub_array_sum_repeated(arr, k, n):
    """
    This function takes in an array, the number of times the array is repeated, and the size of the array.
    It returns the largest sum of a contiguous subarray in the modified array.
    """
    # Initialize the maximum sum as negative infinity
    max_sum = float('-inf')
    # Initialize the current sum as 0
    current_sum = 0
    # Initialize the array size as the size of the input array
    array_size = n

    # Iterate over the array k times
    for _ in range(k):
        # Iterate over the array
        for i in range(array_size):
            # Update the current sum
            current_sum += arr[i]
            # Update the maximum sum if the current sum is greater
            if current_sum > max_sum:
                max_sum = current_sum
            # If the current sum is negative, reset it to 0
            if current_sum < 0:
                current_sum = 0

    return max_sum