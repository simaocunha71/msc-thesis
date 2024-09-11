```
def larg_nnum(lst, n):
    """
    Takes in a list and an integer n and returns a list containing the n largest items from the list.

    Parameters:
        lst (list): The list to be searched through.
        n (int): The number of largest items to return.

    Returns:
        list: The n largest items from the list.
    """
    # Sort the list in descending order
    lst.sort(reverse = True)
    # Return the first n items
    return lst[:n]
```

This function takes in a list and an integer `n` and returns a list containing the `n` largest items from the list. The function first sorts the list in descending order using the `sort()` method with the `reverse` parameter set to `True`. Then, it returns the first `n` items from the sorted list using slicing.

To test the function, you can use the `assert` statement to check if the result of calling the function with the provided example inputs matches the expected output. In this case, the function is called with the list `[10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]` and the integer `2`. The expected output is `[100, 90]`, which represents the two largest items from the list.

By running the test, you can verify that the function correctly returns the `n` largest items from the input list.

Note: The function modifies the original list by sorting it in place. If you want to keep the original list unchanged, you can make a copy of the list before sorting it.

Here's an example of how you can use the `larg_nnum()` function:

```python
numbers = [10, 20, 50, 70, 90, 20, 50, 40, 60, 80, 100]
n = 2
result = larg_nnum(numbers, n)
print(result)  # Output: [100, 90]
