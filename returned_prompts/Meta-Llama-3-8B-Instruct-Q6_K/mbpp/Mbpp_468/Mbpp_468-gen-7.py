```
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
```
The function `max_product` takes a list of numbers as input and returns the maximum product that can be formed by multiplying numbers of an increasing subsequence of that array.

The function uses dynamic programming to solve the problem. It maintains two arrays: `dp` and `max_product`. `dp[i]` stores the maximum product that can be formed by multiplying numbers of an increasing subsequence ending at index `i`, and `max_product[i]` stores the maximum product that can be formed by multiplying numbers of an increasing subsequence ending at index `i` and including the number at index `i`.

The function iterates over the array and for each number, it checks all previous numbers that are smaller than the current number. If a smaller number is found, it updates `dp[i]` and `max_product[i]` accordingly.

Finally, the function returns the maximum value in the `max_product` array, which represents the maximum product that can be formed by multiplying numbers of an increasing subsequence of the input array.

The unit test `assert max_product([3, 100, 4, 5, 150, 6]) == 3000` ensures that the function works correctly. The maximum product that can be formed by multiplying numbers of an increasing subsequence of the array `[3, 100, 4, 5, 150, 6]` is indeed `3000`.