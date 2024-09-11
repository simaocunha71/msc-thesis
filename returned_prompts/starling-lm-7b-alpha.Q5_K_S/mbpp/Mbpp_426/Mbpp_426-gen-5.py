```
def filter_oddnumbers(num_list):
    """
    Filter odd numbers from a given list of numbers

    Parameters
    ----------
    num_list : list
        List of numbers

    Returns
    -------
    list
        List with only odd numbers
    """
    odd_numbers = []
    for num in num_list:
        if num % 2 != 0:
            odd_numbers.append(num)
    return odd_numbers
```

To test the function:

```python
def test_filter_oddnumbers():
    assert filter_oddnumbers([1, 2, 3, 4, 5, 6, 7, 8, 9, 10]) == [1,3,5,7,9]
    print("All test cases passed")

test_filter_oddnumbers()
```

This function iterates through the given list of numbers and adds any odd numbers to a new list. It then returns the new list.

To test this function, a function `test_filter_oddnumbers` is created to call the `filter_oddnumbers` function with a sample list of numbers and assert that the result is the same as the expected result.

The `filter_oddnumbers` function is defined to take a list of numbers as input and returns a list with only odd numbers. It does this by iterating through the input list and checking if each number is odd (i.e., not divisible by 2). If a number is odd, it is added to a new list of odd numbers. Finally, the function returns the new list of odd numbers.

The test cases are then run using the `test_filter_oddnumbers` function, and if all test cases pass, the message "All test cases passed" is printed.

This approach allows for easy testing of the `filter_oddnumbers` function and ensures that it correctly filters odd numbers from a given list of numbers.





























































