Here is the Python function for the problem:

```python
def min_product_tuple(lst):
    return min(x * y for (x, y) in lst)

print(min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]))  # Outputs: 8
```

In this function, we use the `min` function with a generator expression to calculate the product of each pair of numbers in the tuples in the list, and find the smallest product.

This function works by iterating through the list of tuples, for each tuple it takes the product of the two elements (x*y) and returns the minimum of these products.

So, for the list [(2, 7), (2, 6), (1, 8), (4, 9)], it calculates the products as [14, 12, 8, 36], and returns 8 as the smallest.

The time complexity of this function is O(n), as it iterates through the list once