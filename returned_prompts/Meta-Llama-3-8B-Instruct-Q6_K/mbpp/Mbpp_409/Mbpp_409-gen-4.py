```
def min_product_tuple(tuples):
    products = [(a * b) for a, b in tuples]
    return min(products)
```


Here is an explanation of the code:

1. We create a list comprehension to generate a list of products by multiplying each pair of numbers from the input list of tuples.
2. We then use the built-in `min` function to find the smallest product in the list.
3. The result is returned as the minimum product from the pairs of tuples.

The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` ensures that the function works correctly by comparing the output to the expected result of 8, which is the smallest product in the given list of tuples.