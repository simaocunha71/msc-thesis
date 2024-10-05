To solve this problem, you can follow these steps:

1. Check if the input numbers are all integers. If any of the numbers are not integers, return False. You can use the `isinstance()` function to check if a variable is an integer. Here's how you can do it:
```python
if not all(isinstance(x, int) for x in [x, y, z]):
    return False
```
2. Next, calculate the sum of `y` and `z`, and check if it's equal to `x`. If it is, return True. Otherwise, return False. You can use the `==` operator to compare if two values are equal. Here's how you can do it:
```python
if x == (y + z):
    return True
```
3. If the above conditions are not met, return False. Here's how you can do it:
```python
else:
    return False
```
4. Combining all the steps together, the complete solution would look like this:

```python
def any_int(x, y, z):
    '''
    Create a function that takes 3 numbers.
    Returns true if one of the numbers is equal to the sum of the other two, and all numbers are integers.
    Returns false in any other cases.
    
    Examples
    any_int(5, 2, 7) ➞ True
    
    any_int(3, 2, 2) ➞ False
    
    any_int(3, -2, 1) ➞ True
    
    any_int(3.6, -2.2, 2) ➞ False
    '''

    if not all(isinstance(x, int) for x in [x, y, z]):
        return False

    if x == (y + z):
        return True

    else:
        return False
```

You can use this function to check if one of the numbers is equal to the sum of the other two, and all numbers are integers.

Example usage:
```python
print(any_int(5, 2, 7))  #