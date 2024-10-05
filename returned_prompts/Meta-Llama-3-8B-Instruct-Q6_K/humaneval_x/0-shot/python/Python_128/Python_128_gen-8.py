
Here is a Python function that implements the described behavior:

```
def prod_signs(arr):
    if not arr:
        return None
    signs = [1 if x > 0 else -1 if x < 0 else 0 for x in arr]
    product = 1
    for sign in signs:
        product *= sign
    return sum(abs(x) for x in arr) * product
```

Explanation:

1. Check if the input array is empty. If it is, return None.
2. Create a list `signs` where each element is 1 if the corresponding element in the input array is positive, -1 if it's negative, and 0 if it's zero.
3. Calculate the product of all signs in the `signs` list.
4. Calculate the sum of the magnitudes of all elements in the input array using a generator expression.
5. Return the product of the sum of magnitudes and the product of signs.

This function should pass the provided unit tests.