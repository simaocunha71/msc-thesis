Here's a Python function that accomplishes the task:

```python
def unique_product(nums):
    """
    Calculate the product of the unique numbers in a given list.
    """
    unique_nums = set(nums)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```

To verify the function, you can use the `assert` keyword like so:

```python
def test_unique_product():
    assert unique_product([10, 20, 30, 40, 20, 50, 60, 40]) == 720000000

test_unique_product()
```

The `set` function is used to convert the given list of numbers to a set, which automatically removes any duplicate values. Then, a loop iterates over the unique numbers in the set and multiplies each one to the product variable. Finally, the product is returned.

To test the function, a new function called `test_unique_product` is created. Inside this function, the `assert` keyword is used to check if the output of the `unique_product` function with the provided list is equal to the expected result of 720000000. If the assertion is true, no error is raised and the test passes. Otherwise, an `AssertionError` is raised and the test fails.

By executing the `test_unique_product` function, you can verify that the `unique_product` function is working correctly.

```python
def unique_product(nums):
    """
    Calculate the product of the unique numbers in a given list.
    """
    unique_nums = set(nums)
    product = 1
    for num in unique_nums:
        product *= num
    return product
```

The `set` function is used to convert the given list of numbers to a set, which automatically removes any duplicate values. Then, a loop iterates over the unique numbers in the set and multiplies each one to the product variable. Finally, the product is returned.

To test the function, a new function called `test_unique