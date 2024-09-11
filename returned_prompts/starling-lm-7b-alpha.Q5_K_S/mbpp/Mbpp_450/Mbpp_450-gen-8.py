"""
To solve this problem, you can follow the steps below:

1. Define a function called `extract_string` that takes two arguments: `string_list` and `size`.
2. Inside the function, initialize an empty list called `result_list`.
3. Use a for loop to iterate through each string in `string_list`.
4. If the length of the current string is less than or equal to `size`, append the string to `result_list`.
5. Finally, return `result_list`.
6. Test the function by calling `extract_string` with the given input and expected output.

Here's an example implementation of the solution:

```python
def extract_string(string_list, size):
    result_list = []
    for string in string_list:
        if len(string) <= size:
            result_list.append(string)
    return result_list
```

To test the function, you can use the following code:

```python
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
```

This assertion will pass if the `extract_string` function correctly extracts the specified size of strings from the given list.
"""

# Python code:
def extract_string(string_list, size):
    result_list = []
    for string in string_list:
        if len(string) <= size:
            result_list.append(string)
    return result_list

# Test the function
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'], 8) == ['practice', 'solution']
```