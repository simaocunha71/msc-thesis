"""
The function `extract_singly` takes a list of lists as an argument and returns a set of the individual numbers. Here is one possible implementation:

```python
def extract_singly(lst_of_lists):
    # Use the built-in set function to directly convert the list of lists to a set.
    # This will automatically remove any duplicate values.
    return set(lst_of_lists)
```

You can use the `assert` keyword to verify the correctness of the function. The `assert` keyword in Python is used to test if a condition is true. If the condition is false, the program will raise an `AssertionError` with an error message. In this case, the condition is that the set of the `extract_singly` function should be equal to the set of the expected output. If the condition is true, the `assert` statement will not raise an error and the program will continue normally.

Here is an example of how to use the `assert` keyword to verify the correctness of the `extract_singly` function:

```python
def test_extract_singly():
    # The expected output of the `extract_singly` function.
    expected_output = set([3, 4, 5, 7, 1])
    
    # Call the `extract_singly` function with a test input.
    actual_output = extract_singly([(3, 4, 5), (4, 5, 7), (1, 4)])
    
    # Use the `assert` keyword to verify if the actual output is equal to the expected output.
    assert actual_output == expected_output

# Call the `test_extract_singly` function to verify the correctness of the `extract_singly` function.
test_extract_singly()
```
"""

def extract_singly(lst_of_lists):
    # Use the built-in set function to directly convert the list of lists to a set.
    # This will automatically remove any duplicate values.
    return set(lst_of_lists)

def test_extract_singly():
    # The expected output of the `extract_singly` function.
    expected_output = set([3