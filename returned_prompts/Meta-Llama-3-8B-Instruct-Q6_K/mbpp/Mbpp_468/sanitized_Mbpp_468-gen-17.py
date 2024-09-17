def max_product(nums):
    if not nums:
        return 0

    n = len(nums)
    dp = [1] * n
    max_product = [1] * n

    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
                max_product[i] = max(max_product[i], max_product[j] * nums[i])

    return max(max_product)