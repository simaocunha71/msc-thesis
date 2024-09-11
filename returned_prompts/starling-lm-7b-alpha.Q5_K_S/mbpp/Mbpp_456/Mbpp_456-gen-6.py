To solve this problem we need to write a function that will take a list of strings as input and return a new list where each string is reversed. Here's one way to do it:

```python
def reverse_string_list(lst):
    reversed_list = []
    for string in lst:
        reversed_list.append(string[::-1])
    return reversed_list
```

This function works by iterating over each string in the input list and using slicing (with step -1) to reverse each string. The reversed strings are then appended to a new list, which is returned at the end.

To check if the function is working correctly, you can use the `assert` statement to compare the result of calling the function with a known input (`['Red', 'Green', 'Blue', 'White', 'Black']`) to the expected output (`['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`). If the function is working correctly, this `assert` statement will not raise an error.
```python
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```

In this case, the `assert` statement checks if the result of calling `reverse_string_list` with the input `['Red', 'Green', 'Blue', 'White', 'Black']` is equal to the expected output `['deR', 'neerG', 'eulB', 'etihW', 'kcalB']`. If the two lists are not equal, the `assert` statement will raise an error, indicating that the function is not working correctly.

If you want to check the function on a different set of input strings, you can replace `['Red', 'Green', 'Blue', 'White', 'Black']` with the desired input strings.

Note that the `assert` statement is a debugging aid and is typically used in the body of a function or method. It is not intended to be used in the interactive interpreter, as it will raise an `AssertionError` if the condition is False.

Here are some additional examples of how you can