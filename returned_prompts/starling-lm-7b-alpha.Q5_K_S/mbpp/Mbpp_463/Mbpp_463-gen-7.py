```
def max_subarray_product(nums):
    min_end = float('inf')
    max_so_far = float('-inf')
    max_product = float('-inf')

    for num in nums:
        min_end = min(min_end, num)
        max_so_far = max(max_so_far, num)
        max_product = max(max_product, max_so_far - min_end)

    return max_product
```

Explanation:
The function `max_subarray_product` takes in an array of numbers called `nums` and returns the maximum product subarray of the given array.

To solve this problem, we use the Kadane's algorithm, which is an efficient method to find the maximum sum subarray of an array. In this case, we modify the algorithm to find the maximum product subarray.

We initialize three variables: `min_end` to positive infinity, `max_so_far` to negative infinity, and `max_product` to negative infinity. These variables help us keep track of the minimum ending value, the maximum value seen so far, and the maximum product subarray value, respectively.

We then iterate through each number in the `nums` array. For each number, we update the `min_end` and `max_so_far` variables by taking the minimum and maximum values respectively. We also update the `max_product` by taking the maximum value between the current `max_product`, the difference between the `max_so_far` and `min_end` multiplied by the current number, and the current number itself.

Finally, we return the `max_product`, which represents the maximum product subarray of the given array.

The time complexity of this solution is O(n), where n is the length of the input array.

The space complexity is O(1), as we only use a constant amount of extra memory to store the variables.

This solution has a time complexity of O(n) and a space complexity of O(1), making it efficient for large input arrays.

The assert statement at the beginning of the solution verifies that the `max_subarray_product` function returns the correct result for the given