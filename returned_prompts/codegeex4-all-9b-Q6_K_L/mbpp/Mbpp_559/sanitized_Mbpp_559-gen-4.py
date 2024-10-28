def max_sub_array_sum(arr, k):
    """
    This function finds the sum of the largest contiguous sublist in the given list.
    :param arr: List of integers
    :param k: Length of the sublist
    :return: Sum of the largest contiguous sublist
    """
    n = len(arr)
    max_sum = float('-inf')
    for i in range(n - k + 1):
        max_sum = max(max_sum, sum(arr[i:i+k]))
    return max_sum