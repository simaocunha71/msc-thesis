def largest_subset(nums):
    # sort the list in ascending order
    nums.sort()
    # initialize the dp array
    dp = [1] * len(nums)
    # initialize the maximum length of subset
    max_subset_len = 1
    # iterate through the list
    for i in range(1, len(nums)):
        # iterate through the previous elements
        for j in range(i):
            # if the current element is divisible by the previous element
            if nums[i] % nums[j] == 0:
                # update the dp array
                dp[i] = max(dp[i], dp[j] + 1)
                # update the maximum length of subset
                max_subset_len = max(max_subset_len, dp[i])
    # return the maximum length of subset
    return max_subset_len