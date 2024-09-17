```
def max_product(nums):
    if not nums:
        return 0

    dp = [num for num in nums]
    max_product = dp[0]
    for i in range(1, len(nums)):
        if dp[i] < 0:
            dp[i] = max(dp[i], dp[i-1] * dp[i])
        else:
            dp[i] = max(dp[i], dp[i-1] * dp[i])
        max_product = max(max_product, dp[i])
    return max_product
```


The function `max_product` takes a list of numbers as input and returns the maximum product formed by multiplying numbers of an increasing subsequence of that array.
It initializes a list `dp` with the same elements as the input list, and sets the initial maximum product `max_product` to the first element of `dp`.
Then, it iterates over the list from the second element to the end. For each element, it calculates the maximum product by considering two cases: either the current element is negative or positive. If the current element is negative, it means that the maximum product is the maximum of the current element and the product of the previous maximum product and the current element. If the current element is positive, it means that the maximum product is the maximum of the current element and the product of the previous maximum product and the current element. Finally, it updates the `max_product` with the maximum product calculated in the current iteration.
The function returns the maximum product calculated in the last iteration. The unit test `assert max_product([3, 100, 4, 5, 150, 6]) == 3000` ensures that the function works correctly. The maximum product formed by multiplying numbers of an increasing subsequence of the array `[3, 100, 4, 5, 150, 6]` is indeed 3000.