Here is one possible implementation for the function:

```python
def consecutive_duplicates(lst):
    result = []
    for i in range(len(lst)):
        if i == 0 or lst[i] != lst[i-1]:
            result.append(lst[i])
    return result
```

This function iterates through the input list, checking if the current element is the same as the previous one. If it is not, the current element is added to the result list. This ensures that only the first occurrence of each element is kept. The function then returns the resulting list without consecutive duplicates.

You can use the provided assert statement to verify the correctness of the implementation.

```python
assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]) == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```

The assert statement checks if the result of the `consecutive_duplicates` function on the provided list is equal to the expected result. If the assertion is true, the program will continue running. Otherwise, it will raise an error, indicating that the function is incorrect.

This implementation should correctly remove consecutive duplicates from a given list.

```python
print(consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]))  # Output: [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]
```

The provided example demonstrates the usage of the `consecutive_duplicates` function with a sample list. The function removes consecutive duplicates from the list and returns the resulting list, which is then printed.
```

```python
def consecutive_duplicates(lst):
    result = []
    for