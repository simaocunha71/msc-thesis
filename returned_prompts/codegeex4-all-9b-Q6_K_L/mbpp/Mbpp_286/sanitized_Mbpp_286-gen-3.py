def max_sub_array_sum_repeated(arr, k, n):
    """
    This function returns the maximum sum of a contiguous subarray in the modified array which is formed by repeating the given array k times.
    """
    # Calculate the maximum sum of a contiguous subarray in the original array
    max_sum = arr[0]
    current_sum = arr[0]
    for i in range(1, n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)
    # Repeat the array k times and calculate the maximum sum of a contiguous subarray
    repeated_array = arr * k
    max_sum_repeated = repeated_array[0]
    current_sum_repeated = repeated_array[0]
    for i in range(1, n * k):
        current_sum_repeated = max(repeated_array[i], current_sum_repeated + repeated_array[i])
        max_sum_repeated = max(max_sum_repeated, current_sum_repeated)
    # Return the maximum sum of a contiguous subarray in the modified array
    return max_sum_repeated