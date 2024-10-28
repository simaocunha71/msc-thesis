def max_sub_array_sum(arr, n):
    """
    This function finds the sum of the largest contiguous sublist in the given list.

    Args:
    arr (list): The input list of integers.
    n (int): The length of the input list.

    Returns:
    int: The sum of the largest contiguous sublist.
    """
    max_sum = float('-inf')
    current_sum = 0

    for i in range(n):
        current_sum = max(arr[i], current_sum + arr[i])
        max_sum = max(max_sum, current_sum)

    return max_sum