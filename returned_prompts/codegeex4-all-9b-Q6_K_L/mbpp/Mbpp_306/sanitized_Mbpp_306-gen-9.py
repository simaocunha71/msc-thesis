def max_sum_increasing_subseq(arr, n, i, k):
    """
    :param arr: List of integers
    :param n: Length of array
    :param i: Index of prefix
    :param k: Index of kth element
    :return: Maximum sum of increasing subsequence from prefix until ith index and including kth element
    """
    if k <= i:
        return -1

    # Initialize dp array
    dp = [0] * (n + 1)

    # Calculate dp values
    for j in range(1, n + 1):
        if j <= i:
            dp[j] = arr[j - 1]
        else:
            dp[j] = arr[j - 1] + dp[j - 1]

    # Find maximum sum
    max_sum = 0
    for j in range(1, n + 1):
        if j <= i:
            max_sum = max(max_sum, dp[j])
        else:
            max_sum = max(max_sum, dp[j] + arr[k - 1])

    return max_sum