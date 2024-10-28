```
def div_list(list1, list2):
    return [i/j for i, j in zip(list1, list2)]
```
This function uses list comprehension and the built-in `zip` function to iterate over the two lists in parallel. It then divides each corresponding element from the two lists and returns the result as a new list.

For example, if we have the lists `[4, 5, 6]` and `[1, 2, 3]`, the function would return the list `[4.0, 2.5, 2.0]`, as expected. The unit test `assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]` ensures that this is the case. 

Note that this function assumes that the two lists are of the same length, and that the second list does not contain zeros (since division by zero is undefined). If these conditions are not met, the function may raise an error or return incorrect results. 

In practice, you might want to add error checking to handle these cases. For example, you could check that the lists are of the same length and that the second list does not contain zeros before attempting to divide. You could also consider using a try-except block to catch and handle any division by zero errors that might occur. 
```python
def div_list(list1, list2):
    if len(list1) != len(list2):
        raise ValueError("Lists must be of the same length")
    result = []
    for i, j in zip(list1, list2):
        if j == 0:
            raise ValueError("Cannot divide by zero")
        result.append(i/j)
    return result
``` 
This version of the function will raise a `ValueError` if the lists are of different lengths or if the second list contains a zero. It will return the result of the division for each pair of corresponding elements if these conditions are met. 
```python
print(div_list([4,5,6],[1, 2, 3]))  # Output: [4.0, 2.5, 2.0]
print(div_list([4,5,6],[1, 0, 3]))  # Raises ValueError: Cannot divide by zero
print(div_list([4,5,6],[1, 2, 4]))  # Raises ValueError: Lists must be of the