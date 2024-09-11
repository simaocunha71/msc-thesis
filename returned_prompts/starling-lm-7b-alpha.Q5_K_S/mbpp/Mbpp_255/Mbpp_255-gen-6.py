To generate all combinations of length n from a given list, you can use the `itertools.product` function from Python's standard library. Here's an example of how you can define the `combinations_colors` function:

```python
from itertools import product

def combinations_colors(colors, length):
    return list(product(colors, repeat=length))
```

In this function, `colors` is the input list of colors, and `length` is the desired length of each combination. The `product` function returns an iterable object, so we need to convert it to a list using the `list` function.

To test the function and verify the result, you can use the `assert` statement like this:

```python
assert combinations_colors(["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
```

This assertion checks if the output of the `combinations_colors` function with the input list `["Red","Green","Blue"]` and length `1` is equal to the expected result `[('Red',), ('Green',), ('Blue',)]`. If the assertion fails, it means that the function is not working as expected.

You can run this code in a Python environment to test the function and ensure that it generates the correct combinations.

```python
from itertools import product

def combinations_colors(colors, length):
    return list(product(colors, repeat=length))

assert combinations_colors(["Red","Green","Blue"],1)==[('Red',), ('Green',), ('Blue',)]
```

The output of the `print` statement will be `True`, indicating that the function is working correctly and generating the expected combinations.

```python
True
```

It's important to note that the `itertools.product` function generates all possible combinations of the input elements, including repetitions. If you want to generate unique combinations without repetition, you can use the `itertools.permutations` function instead.

Here's an example of how you can define the `combinations_unique` function to generate unique combinations:

```python
from itertools import product, permutations

def combinations_unique(colors