def max_product(nums):
    # Initialize the dp array with 1s
    dp = [1] * len(nums)

    # Iterate through the array
    for i in range(1, len(nums)):
        # Iterate through the previous indices
        for j in range(i):
            # If the current number is greater than the previous number, update the dp array
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])

    # Return the maximum product
    return max(dp)