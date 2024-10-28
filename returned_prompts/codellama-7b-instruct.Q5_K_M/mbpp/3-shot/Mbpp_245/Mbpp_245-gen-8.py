
def max_sum(arr):
    n = len(arr)
    if n == 0:
        return 0
    if n == 1:
        return arr[0]
    if n == 2:
        return max(arr[0], arr[1])

    # Initialize the maximum sum for the first subsequence
    # and its corresponding ending index
    max_sum_first, end_index = max(
        (sum(arr[0:i + 1]), i) for i in range(n))

    # Initialize the maximum sum for the second subsequence
    # and its corresponding ending index
    max_sum_second, start_index = max(
        (sum(arr[i:]), i) for i in range(n))

    # If the first subsequence is bitonic, then the maximum sum
    # is the sum of the first subsequence
    if arr[end_index] > arr[start_index]:
        return max_sum_first

    # If the second subsequence is bitonic, then the maximum sum
    # is the sum of the second subsequence
    if arr[end_index] < arr[start_index]:
        return max_sum_second

    # If neither of the two subsequences is bitonic, then the maximum
    # sum is the maximum of the two sums
    return max(max_sum_first, max_sum_second)


