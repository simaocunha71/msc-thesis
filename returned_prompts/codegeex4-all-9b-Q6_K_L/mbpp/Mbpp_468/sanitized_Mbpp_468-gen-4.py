def max_product(nums):
    """
    Finds the maximum product formed by multiplying numbers of an increasing subsequence of the array.
    :param nums: List[int]
    :return: int
    """
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n  # Initialize dp array with 1

    # Compute maximum product for increasing subsequences
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])

    # Find the maximum product from the dp array
    max_product = max(dp)
    return max_product