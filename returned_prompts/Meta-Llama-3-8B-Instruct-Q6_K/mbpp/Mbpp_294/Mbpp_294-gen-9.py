The problem is asking to find the maximum value in a given heterogeneous list. However, the problem statement does not specify the type of the maximum value. 

Thanks to the unit test `assert max_val(['Python', 3, 2, 4, 5, 'version'])==5`, we can infer that the problem is asking to find the maximum integer value in the list. 

Here is a Python solution for this problem:

```
python
def max_val(lst):
    max_val = float('-inf')
    for val in lst:
        if isinstance(val, int) and val > max_val:
            max_val = val
    return max_val
```

This function iterates over the list, checks if each value is an integer, and if it's greater than the current maximum value, updates the maximum value. The function returns the maximum value found. 

The `isinstance(val, int)` function is used to check if the value is an integer, and the `float('-inf')` is used to initialize the maximum value as negative infinity. This ensures that the first integer value in the list will be considered as the maximum value. 

The function works correctly even if the list contains non-integer values, as it ignores them and only considers the integer values.  For example, if the list contains a string 'Python', the function will ignore it and find the maximum integer value in the list.  If the list does not contain any integer values, the function will return negative infinity.  However, based on the unit test, we can infer that the function should return the maximum value that can be found in the list.  Therefore, the function can be modified to return the maximum value found, or to return a message indicating that no maximum value was found.  The modified function is shown below:

```
python
def max_val(lst):
    max_val = float('-inf')
    for val in lst:
        if isinstance(val, int):
            max_val = max(max_val, val)
    return max_val if max_val != float('-inf') else 'No maximum value found'
```  This function will return the maximum integer value found in the list, or the message 'No maximum value found' if no integer values were found in the list.  The function works correctly even if the list contains non-integer values, as it ignores them and only considers the integer values.  The unit test `assert max_val(['Python', 3, 2, 4, 