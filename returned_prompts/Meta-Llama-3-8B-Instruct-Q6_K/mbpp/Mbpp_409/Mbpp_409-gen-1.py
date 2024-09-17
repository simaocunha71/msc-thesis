You can solve this problem by using the built-in min function in Python, which returns the smallest item in an iterable or the smallest of two or more arguments.

Here is the Python function that solves the problem:
```
def min_product_tuple(tuples):
    return min(t[0] * t[1] for t in tuples)
```
This function takes a list of tuples as input and returns the minimum product of the pairs of numbers in the tuples.

The unit test `assert min_product_tuple([(2, 7), (2, 6), (1, 8), (4, 9)] )==8` ensures that the function works correctly. It checks if the minimum product of the pairs of numbers in the given list is 8, which is the expected output.

You can use this function to find the minimum product from the pairs of tuples within a given list. For example:
```
tuples = [(2, 7), (2, 6), (1, 8), (4, 9)]
min_product = min_product_tuple(tuples)
print(min_product)  # Output: 8
```


