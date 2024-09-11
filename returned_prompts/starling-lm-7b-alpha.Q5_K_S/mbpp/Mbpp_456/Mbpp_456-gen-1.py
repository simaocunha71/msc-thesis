Here's a Python function that reverses each string in a given list of strings:

```python
def reverse_string_list(s_list):
    return [s[::-1] for s in s_list]
```

To test it, you can use the provided assertion:

```python
assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```

The `[::-1]` slice syntax is used to reverse the string. It starts at the end of the string and goes backwards with a step size of -1, effectively reversing the string. The list comprehension is used to apply the `[::-1]` slice to each string in the input list.

The `assert` statement is used to verify if the function correctly reverses the strings in the given list. If the function doesn't work as expected, the `assert` statement will raise an `AssertionError` with an error message explaining the failure.

This solution is efficient and simple, with a time complexity of O(n) and a space complexity of O(1), where n is the number of strings in the input list.

"""

def reverse_string_list(s_list):
    return [s[::-1] for s in s_list]

assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']
```

This Python function will correctly reverse each string in a given list of strings.

The `[::-1]` slice syntax is used to reverse the strings. It starts at the end of the string and goes backwards with a step size of -1, effectively reversing the string. The list comprehension is used to apply the `[::-1]` slice to each string in the input list.

The `assert` statement is used to verify if the function correctly reverses the strings in the given list. If the function doesn't work as expected, the `assert` statement will raise an `AssertionError` with an error message explaining the failure.