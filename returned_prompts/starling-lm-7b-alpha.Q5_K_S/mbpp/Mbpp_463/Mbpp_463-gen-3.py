```
def max_subarray_product(nums):
    max_product = nums[0]
    min_product = nums[0]
    cur_product = nums[0]
    for i in range(1, len(nums)):
        cur_product = max(nums[i], cur_product * nums[i], min_product * nums[i])
        max_product = max(cur_product, max_product)
        min_product = min(cur_product, min_product)
    return max_product
```

Explanation:
The maximum product subarray of the given array is the subarray with the largest product, where all the numbers in the subarray are positive, or all the numbers are negative and have the same sign.

In the implementation, we maintain three variables:
- `max_product`: the maximum product subarray ending at the current index.
- `min_product`: the minimum product subarray ending at the current index.
- `cur_product`: the product of the subarray ending at the current index.

We initialize `max_product`, `min_product`, and `cur_product` to the first number of the array. Then, we iterate through the array from the second number. For each number, we update `cur_product` by taking the maximum of the current number, the product of the current number and `cur_product`, and the product of the current number and `min_product`. This ensures that we always have the maximum product subarray ending at the current index. We also update `max_product` and `min_product` to keep track of the maximum and minimum product subarrays. Finally, we return the maximum product subarray.

The time complexity of this solution is O(n), where n is the length of the input array, and the space complexity is O(1), as we only use a constant amount of extra space.

To verify the solution, we can compare the result of `max_subarray_product` with the expected maximum product subarray using the `assert` statement.

The provided assertion `assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112` checks if the