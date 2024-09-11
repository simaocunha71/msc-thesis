def max_sum(nums):
    """
    Complexity: O(n)
    """
    dp = [0] * len(nums)
    for i in range(len(nums)):
        dp[i] = nums[i]
    for i in range(1, len(nums)):
        dp[i] = max(nums[i] + dp[i-1], dp[i])
    return dp[-1]


# assert max_sum([1, 15, 51, 45, 33, 100, 12, 18, 9]) == 194
# assert max_sum([1, 1, 5, 3, 4, 2]) == 7
# assert max_sum([3, 2, 4, 1]) == 7
# assert max_sum([3, 10, 4, 1]) == 14
# assert max_sum([-1, 2, 3, 4]) == 7
# assert max_sum([-1, 2, 3, -4]) == 3
# assert max_sum([-1, 2, 3, -4, 1]) == 3
# assert max_sum([-1, 2, 3, -4, 1, 10]) == 11
# assert max_sum([-1, 2, 3, -4, 1, -10]) == 4
# assert max_sum([-1, 2, 3, -4, 1, -10, 5]) == 9
# assert max_sum([-1, 2, 3, -4, 1, -10, -5]) == 4
# assert max_sum([-1, 2, 3, -4, 1, -10, -5, -100]) == 4

# print(max_sum([-1, 2, 3, -4, 1, -10, -5]))
# print(max_sum([-1, 2, 3, -4, 1, -10,