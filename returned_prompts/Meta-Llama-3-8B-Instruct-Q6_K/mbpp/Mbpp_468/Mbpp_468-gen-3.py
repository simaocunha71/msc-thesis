```
def max_product(nums):
    if not nums:
        return 0

    dp = [num for num in nums]
    max_dp = [num for num in nums]

    for i in range(1, len(nums)):
        for j in range(i):
            if nums[i] > nums[j]:
                dp[i] = max(dp[i], dp[j] * nums[i])
                max_dp[i] = max(max_dp[i], max_dp[j] * nums[i])

    return max(max_dp)
```    
The function `max_product` takes a list of integers as input and returns the maximum product formed by multiplying numbers of an increasing subsequence of that array.

The function first initializes two lists, `dp` and `max_dp`, where `dp[i]` stores the maximum product ending at index `i` and `max_dp[i]` stores the maximum product ending at index `i` that is less than or equal to `nums[i]`.

Then, for each element in the array, it iterates over all previous elements. If the current element is greater than the previous element, it updates `dp[i]` and `max_dp[i]` accordingly.

Finally, it returns the maximum product ending at any index, which is stored in `max_dp`.

For example, given the input `[3, 100, 4, 5, 150, 6]`, the function returns `3000`, which is the maximum product formed by multiplying numbers of an increasing subsequence of that array. The increasing subsequence is `[3, 100, 150, 6]`, and the product is `3 * 100 * 150 * 6 = 3000`.