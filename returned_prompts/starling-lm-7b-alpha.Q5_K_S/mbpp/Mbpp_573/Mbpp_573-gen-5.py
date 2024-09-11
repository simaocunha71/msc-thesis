Here's one way you could write the function:

```python
def unique_product(numbers):
    return reduce(lambda x, y: x * y, set(numbers))
```

This function uses Python's built-in `reduce` function to multiply all the numbers in the set. The `reduce` function applies a binary function to the elements of an iterable in a way that reduces the iterable to a single value.

In this case, the binary function is a lambda that takes two arguments, `x` and `y`, and multiplies them together (`x * y`). The iterable is a set created from the input list of numbers. The set eliminates duplicate numbers, ensuring that only unique numbers are multiplied together.

Finally, the function returns the result of the multiplication.

You can test the function with the provided assertion to verify that it works correctly:

```python
assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) ==  720000000
```

This assertion asserts that the function `unique_product` correctly calculates the product of the unique numbers in the input list `[10, 20, 30, 40, 20, 50, 60, 40]`, which should be `720000000`. If the function is implemented correctly, the assertion will pass and no error will be raised.

Here's a step-by-step breakdown of how the function works:

1. The `set` function is used to create a set from the input list of numbers. This eliminates any duplicate numbers, ensuring that only unique numbers are included in the set.
2. The `reduce` function is used to apply the binary function (a lambda that multiplies two numbers together) to all the numbers in the set. The `reduce` function takes two arguments: the binary function and the iterable (in this case, the set of unique numbers).
3. The `reduce` function applies the binary function to the first two elements of the iterable, then applies it to the result and the next element, and so on, until all elements of