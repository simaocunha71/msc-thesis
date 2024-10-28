```
def max_product(arr):
    if not arr:
        return 0
    dp = [0] * len(arr)
    dp[0] = arr[0]
    max_product = dp[0]
    for i in range(1, len(arr)):
        dp[i] = max(arr[i], dp[i-1] * arr[i])
        max_product = max(max_product, dp[i])
    return max_product
```    
The problem is to find the maximum product formed by multiplying numbers of an increasing subsequence of the given array.

The given unit test `assert max_product([3, 100, 4, 5, 150, 6]) == 3000` suggests that we need to find the maximum product formed by multiplying numbers of an increasing subsequence. For example, the maximum product in the array [3, 100, 4, 5, 150, 6] is 3000, which is formed by the increasing subsequence [100, 150].

We can solve this problem by using dynamic programming. We maintain an array `dp` where `dp[i]` represents the maximum product formed by multiplying numbers of an increasing subsequence ending at index `i`. We initialize `dp[0]` to `arr[0]` and `max_product` to `dp[0]`.

Then, for each `i` from 1 to `len(arr)`, we calculate `dp[i]` as the maximum of `arr[i]` and `dp[i-1] * arr[i]`. This is because the maximum product formed by multiplying numbers of an increasing subsequence ending at `i` is either the product of the current number and the maximum product formed by multiplying numbers of an increasing subsequence ending at `i-1`, or the current number itself.

Finally, we return `max_product` as the maximum product formed by multiplying numbers of an increasing subsequence. The time complexity of this solution is O(n), where `n` is the length of the array. The space complexity is O(n) as well.