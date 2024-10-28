```
def consecutive_duplicates(lst):
    result = []
    for num in lst:
        if not result or num != result[-1]:
            result.append(num)
    return result
```
The problem is asking to create a function that removes consecutive duplicates from a given list. The function should return a new list with the consecutive duplicates removed, but it should keep the last occurrence of each duplicate.

The unit test provided suggests that the function should keep the last occurrence of each duplicate. For example, in the list [0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4], the function should return [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4].

Here is a Python solution for this problem:
```
def consecutive_duplicates(lst):
    result = []
    for num in lst:
        if not result or num != result[-1]:
            result.append(num)
    return result
```
This function iterates over the input list and appends each number to the result list only if it is different from the last number in the result list. This ensures that consecutive duplicates are removed, but the last occurrence of each duplicate is kept. The function returns the resulting list.