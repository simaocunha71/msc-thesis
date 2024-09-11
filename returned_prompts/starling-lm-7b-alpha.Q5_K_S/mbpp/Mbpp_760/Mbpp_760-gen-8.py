def unique_Element(input_list):
    if len(set(input_list)) == 1:
        return True
    else:
        return False

# Testing the function
print(unique_Element([1,1,1]))  # Should print: True
print(unique_Element([1,1,2]))  # Should print: False

# Assert the function
assert unique_Element([1,1,1]) == True
assert unique_Element([1,1,2]) == False

# More assertions can be added

"""
In the provided Python function, the function checks whether a given list of numbers contains only one distinct element or not by using the built-in Python function set(). The set() function in Python returns a new set with unique elements from the iterable provided as an argument. By converting the input_list to a set, any duplicate elements are removed, and the length of the set is equal to the number of distinct elements in the list. If the length of the set is equal to 1, it means the list contains only one distinct element, and the function returns True. Otherwise, it returns False.
"""

"""
The provided Python function can be tested by using the print() function to print the result of the function with different input lists. The function can also be asserted using the built-in Python assert keyword to ensure that the function returns the expected result for the given test cases.
"""

```python
def unique_Element(input_list):
    if len(set(input_list)) == 1:
        return True
    else:
        return False

# Testing the function
print(unique_Element([1,1,1]))  # Should print: True
print(unique_Element([1,1,2]))  # Should print: False

# Assert the function
assert unique_Element([1,1,1]) == True
assert unique_Element([1,1,2]) == False

# More assertions can be added
```

```python
"""
The Python function unique_Element(input_list) takes a list of numbers as an argument and checks whether the list contains only one distinct element or not. It does this by converting the input_list to a set using the set() function, which removes any duplicate elements