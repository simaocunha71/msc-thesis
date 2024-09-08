Here is the Python function for the problem:

```python
def max_product_tuple(lst):
    max_product = float('-inf')
    for tup in lst:
        product = abs(tup[0] * tup[1])
        if product > max_product:
            max_product = product
    return max_product

assert max_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)]) == 36
```

This function works by iterating over the tuples in the list, calculating the absolute product of the numbers in each tuple, and comparing it to the current maximum product. If the calculated product is larger, it's saved as the new maximum product. The maximum product is then returned after all tuples have been checked.

In the provided assertion, the function correctly returns 36, the maximum absolute product of any pair of numbers in the given list of t