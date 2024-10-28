def max_sub_array_sum_repeated(arr, k, size):
    """
    Function to find the largest sum of a contiguous array in the modified array which is formed by repeating the given array k times.
    :param arr: List of integers
    :param k: Number of times the array is repeated
    :param size: Size of the original array
    :return: Maximum sum of a contiguous array in the modified array
    """
    # Initialize variables
    max_so_far = float('-inf')
    max_ending_here = 0

    # Iterate through the array
    for i in range(len(arr) * k):
        # Update max_ending_here
        max_ending_here += arr[i % size]

        # Update max_so_far if max_ending_here is greater
        if max_ending_here > max_so_far:
            max_so_far = max_ending_here

        # If max_ending_here is negative, reset it to 0
        if max_ending_here < 0:
            max_ending_here = 0

    return max_so_far