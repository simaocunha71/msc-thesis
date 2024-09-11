Here is one possible solution to find the maximum product subarray of the given array:

```python
def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = 1
    for i in range(len(nums)):
        if nums[i] < 0:
            min_product, max_product = max_product, min_product
        max_product = max(nums[i], max_product * nums[i])
        min_product = min(nums[i], min_product * nums[i])
    return max(max_product, min_product)
```

Explanation:
The function `max_subarray_product` takes an array `nums` as input and returns the maximum product of a subarray in the given array. It initializes `max_product` and `min_product` with negative infinity and 1 respectively.

Then, it iterates through the array `nums` using a for loop. For each element in the array, it checks if the element is negative. If it is negative, it swaps the values of `max_product` and `min_product`. This is done to handle the case where the maximum product subarray contains multiple negative numbers.

Next, it updates the `max_product` by taking the maximum between the current element and the product of the current element and `max_product`. This step ensures that `max_product` always holds the maximum product seen so far.

Similarly, it updates the `min_product` by taking the minimum between the current element and the product of the current element and `min_product`. This step ensures that `min_product` always holds the minimum product seen so far.

Finally, it returns the maximum between `max_product` and `min_product`. This is done to handle the case where the maximum product subarray contains only negative numbers.

The time complexity of this solution is O(n), where n is the length of the input array, as it iterates through the array once.

The space complexity of this solution is O(1), as it uses only a constant amount of additional space for the variables `max_product` and `min_product`.

The solution correctly handles the edge case where