def max_product(arr):
    n = len(arr)
    # Initialize dp array with 1
    dp = [1] * n

    # Initialize maximum product
    max_product = arr[0]

    # Iterate through the array
    for i in range(1, n):
        # Iterate through the previous elements
        for j in range(i):
            # Check if the current element is greater than the previous element
            if arr[i] > arr[j]:
                # Update the dp array with the maximum product
                dp[i] = max(dp[i], dp[j] * arr[i])

        # Update the maximum product
        max_product = max(max_product, dp[i])

    return max_product