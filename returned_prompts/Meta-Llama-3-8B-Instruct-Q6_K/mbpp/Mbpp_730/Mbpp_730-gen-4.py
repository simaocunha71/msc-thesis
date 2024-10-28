```
def consecutive_duplicates(lst):
    result = [lst[0]]
    for item in lst[1:]:
        if item != result[-1]:
            result.append(item)
    return result
```
The function `consecutive_duplicates` takes a list `lst` as input. It initializes an empty list `result` with the first element of `lst`. Then it iterates over the rest of `lst`. If the current element is not equal to the last element of `result`, it appends the current element to `result`. Finally, it returns `result`, which is the list with consecutive duplicates removed.

The unit test `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]` ensures that the function works correctly. It checks that the output of `consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])` is equal to `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`. This test covers the case where there are multiple consecutive duplicates of the same element. 