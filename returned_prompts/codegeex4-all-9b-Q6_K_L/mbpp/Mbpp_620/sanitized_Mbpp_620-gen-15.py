def largest_subset(nums):
    # Initialize the dp array with 1s, as each element can be a subset by itself
    dp = [1] * len(nums)
    # Initialize the result to 1, as the smallest subset size is 1
    res = 1
    # Iterate through the list of numbers
    for i in range(len(nums)):
        # Iterate through the previous elements to check for divisibility
        for j in range(i):
            # If the current number is divisible by a previous number, update the dp array
            if nums[i] % nums[j] == 0:
                dp[i] = max(dp[i], dp[j] + 1)
                # Update the result if a larger subset size is found
                res = max(res, dp[i])
    return res