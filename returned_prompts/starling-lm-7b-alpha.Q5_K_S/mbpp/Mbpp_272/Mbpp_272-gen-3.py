"""
def rear_extract(tuples):
    return [t[2] for t in tuples]

# Testing
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
"""

# Explanation
"""
The function `rear_extract` is defined to take in a list of tuples. It uses list comprehension to return a new list that contains only the third element (index 2) of each tuple in the input list. The assert statement checks if the function returns the expected output given the example input.
"""

# Code
```python
def rear_extract(tuples):
    return [t[2] for t in tuples]
```

# Testing
```python
assert rear_extract([(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]) == [21, 20, 19]
```

# Explanation
The `rear_extract` function takes in a list of tuples and uses list comprehension to return a new list containing only the third element (index 2) of each tuple in the input list. The `assert` statement checks if the function returns the expected output when given the example input.

# Example usage
```python
input_list = [(1, 'Rash', 21), (2, 'Varsha', 20), (3, 'Kil', 19)]
result = rear_extract(input_list)
print(result)  # Output: [21, 20, 19]
```

In this example, the `rear_extract` function is called with the `input_list` as the argument. The function returns a new list `[21, 20, 19]`, which is assigned to the variable `result`. The `print` statement outputs the value of `result` to the console.

# Time complexity
The time complexity of the `rear_extract` function is O(n), where n is the number of tu