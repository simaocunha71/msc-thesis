```
def reverse_string_list(lst):
    return [s[::-1] for s in lst]
```
The problem is asking to create a function that takes a list of strings as input and returns a new list where each string in the original list is reversed.

The unit test `assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black'])==['deR', 'neerG', 'eulB', 'etihW', 'kcalB']` helps to clarify the problem.

The solution uses a list comprehension to create a new list where each string is reversed using slicing with a step of -1 (`s[::-1]`). This is a common and efficient way to reverse a string in Python. The function takes a list of strings as input, applies the reversal operation to each string, and returns the resulting list.