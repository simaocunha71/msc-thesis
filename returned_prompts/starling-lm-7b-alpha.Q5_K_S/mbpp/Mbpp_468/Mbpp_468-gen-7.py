```
def max_product(nums):
    best_product = 1
    cur_product = 1
    for i in nums:
        cur_product = max(cur_product * i, i)
        best_product = max(best_product, cur_product)
    return best_product
```

It's O(n).

Explanation:

The key to this problem is that the maximum product will always be an increasing subsequence. Therefore, we can simply maintain the current product and the best product.

Here are the steps:

1. Initialize the current product and the best product to 1.
2. For each number in the array, update the current product by taking the maximum of the current product multiplied by the number, and the number itself. This is because if the number is larger than the current product, then we should only consider the new number. Otherwise, we should consider the product of the current product and the number.
3. Update the best product by taking the maximum of the current product and the best product. This is because the current product might be larger than the best product, or the current product might be a part of a larger increasing subsequence.
4. After all the numbers have been processed, return the best product as the result.

The time complexity of the algorithm is O(n) because we only need to process each number once.

The space complexity is O(1) because we only need to maintain two variables.

Here's a Python implementation of the algorithm:

```python
def max_product(nums):
    best_product = 1
    cur_product = 1
    for i in nums:
        cur_product = max(cur_product * i, i)
        best_product = max(best_product, cur_product)
    return best_product
```

This implementation is straightforward and should pass all the test cases.

Note that this algorithm assumes that the input array is non-negative. If the input array can have negative numbers, a different algorithm would be needed.

In addition, the algorithm assumes that the input array is not empty. If the array can be empty, we need to handle this case separately.

Finally, this algorithm does not guarantee the shortest increasing subsequence