def div_list(a,b):
    if len(a) != len(b):
        return "Error"
    c = []
    for i in range(len(a)):
        c.append(a[i]/b[i])
    return c

# Test
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
print("All tests passed!")





"""
The error in the initial code was that the division of the elements of the two input lists was not being stored anywhere. To fix this, we added a new list `c` to store the division results. We also added a `for` loop to iterate through the indices of the input lists, and for each index, we divide the corresponding elements of the input lists and append the result to `c`. Finally, we return `c`.

To test the function, we used the `assert` statement to check if the function returns the expected result for the given input lists `[4,5,6]` and `[1, 2, 3]`. If the assertion is true, it means that the function is working correctly and all tests passed. Otherwise, an error message will be displayed.
"""

"""
To use this solution, you can call the `div_list` function with two input lists as arguments. The function will divide the elements of the input lists element-wise and return a new list containing the results. Make sure that the input lists have the same length, otherwise the function will return an error message.
"""

```python
def div_list(a,b):
    if len(a) != len(b):
        return "Error"
    c = []
    for i in range(len(a)):
        c.append(a[i]/b[i])
    return c
```

```python
assert div_list([4,5,6],[1, 2, 3])==[4.0,2.5,2.0]
print("All tests passed!")
```

```python
result = div_list([10, 20, 30], [5, 10, 15])
