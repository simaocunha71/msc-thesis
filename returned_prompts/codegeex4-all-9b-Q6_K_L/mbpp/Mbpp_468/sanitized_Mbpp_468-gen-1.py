def max_product(arr):
    n = len(arr)
    dp = [1] * n

    # Initialize the maximum product to be the first element
    max_product = arr[0]

    for i in range(1, n):
        # Find the maximum product of an increasing subsequence ending at index i
        for j in range(i):
            if arr[j] < arr[i]:
                dp[i] = max(dp[i], dp[j] * arr[i])

        # Update the maximum product
        max_product = max(max_product, dp[i])

    return max_product