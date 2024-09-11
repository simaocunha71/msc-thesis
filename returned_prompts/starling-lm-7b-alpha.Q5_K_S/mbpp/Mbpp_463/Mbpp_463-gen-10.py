"""
Here's a simple Python solution:

```python
def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')
    for num in nums:
        max_product = max(max_product * num, num)
        min_product = min(min_product * num, num)
    return max(0, max_product)
```

The time complexity of this algorithm is O(n) where n is the length of the array, and the space complexity is O(1).

The algorithm works by maintaining two variables, `max_product` and `min_product`, initialized as negative infinity and positive infinity respectively. We iterate through the array, updating `max_product` and `min_product` as we go. The product is updated by taking the maximum/minimum of the product of the current element and the current maximum/minimum product, or the current element itself. This ensures that even if the current element is negative, the product is updated correctly. At the end, we return the maximum product subarray, or 0 if the product is negative.
"""

def max_subarray_product(nums):
    max_product = float('-inf')
    min_product = float('inf')
    for num in nums:
        max_product = max(max_product * num, num)
        min_product = min(min_product * num, num)
    return max(0, max_product)

# Assert
assert max_subarray_product([1, -2, -3, 0, 7, -8, -2]) == 112
```

```

```