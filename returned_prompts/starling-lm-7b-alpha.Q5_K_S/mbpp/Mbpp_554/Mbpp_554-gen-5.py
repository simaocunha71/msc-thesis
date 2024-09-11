```
def Split(x):
    new_list = []
    for i in x:
        if i % 2 != 0:
            new_list.append(i)
    return new_list
```

This function works by iterating over the input list and checking whether each number is odd or not. If the number is odd, it is added to the new list. Finally, the new list is returned.

However, Python provides a more concise and efficient method for achieving the same result using list comprehension. Here's how you can rewrite the function using list comprehension:
```python
def Split(x):
    return [i for i in x if i % 2 != 0]
```
In this version of the function, the list comprehension `[i for i in x if i % 2 != 0]` is used to create a new list that only includes the odd numbers from the input list `x`. This is a more Pythonic way to filter a list and is generally more efficient.

To test the function, you can use the `assert` statement to ensure that the function returns the expected result for the given input:
```python
assert Split([1,2,3,4,5,6]) == [1,3,5]
```
The `assert` statement checks if the left-hand side (`Split([1,2,3,4,5,6])`) is equal to the right-hand side (`[1,3,5]`). If the two sides are not equal, an `AssertionError` is raised, indicating that the function is not working correctly.

Overall, this solution provides a way to create a Python function that returns only the odd numbers from a given list of integers, and also demonstrates how to use the `assert` statement to test the function's correctness.

```python
def Split(x):
    return [i for i in x if i % 2 != 0]

assert Split([1,2,3,4,5,6]) == [1,3,5]
```

This code will output `True` if the function is working correctly, and `False` if there is an error in the function.

```python