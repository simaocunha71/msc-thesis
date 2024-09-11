Here's a Python function to interchange the first and last elements in a list:

```python
def swap_List(list1):
    return list1[0], list1[-1], list1[1:-1]
```

This function takes a list as an input and returns a new list with the first and last elements swapped. The `return` statement returns a tuple containing the first and last elements of the list, followed by the remaining elements of the list. The `list1[0]` and `list1[-1]` are the first and last elements of the list respectively. The `list1[1:-1]` is a slice of the list that excludes the first and last elements.

To test this function, you can use the `assert` statement to verify that the function returns the expected result for the given list `[12, 35, 9, 56, 24]`. The expected result is `[24, 35, 9, 56, 12]`.

Here's an example of how you can use this function and the `assert` statement to verify the expected result:

```python
def test_swap_list():
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]

test_swap_list()
```

When you run this code, the `assert` statement will check if the function returns the expected result. If the result is correct, the `assert` statement will not raise an exception and the code will continue executing. If the result is incorrect, the `assert` statement will raise an `AssertionError` exception, indicating that the test has failed.

Note: It's important to use the `assert` statement in a controlled environment, such as in a test function or a test suite, to avoid unexpected `AssertionError` exceptions when running your code in a production environment.

```python

```
Here's a Python function to interchange the first and last elements in a list:

```python
def swap_List(list1):
    return list1[0], list1[-1], list1[1:-1