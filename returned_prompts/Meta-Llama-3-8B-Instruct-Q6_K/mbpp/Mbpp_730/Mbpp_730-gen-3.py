```
def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result
```
The problem is asking to remove consecutive duplicates from a given list. For example, if the input list is `[0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4]`, the output should be `[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`.

The unit test provided helps to understand the problem better. The test case is `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]`. This test case shows that the function should remove consecutive duplicates and keep the last occurrence of each element.

Here is the solution:
```
def consecutive_duplicates(lst):
    result = []
    for i in lst:
        if not result or i != result[-1]:
            result.append(i)
    return result
```
This function iterates over the input list and checks if the current element is different from the last element in the result list. If it is different, it adds the current element to the result list. This way, consecutive duplicates are removed and the last occurrence of each element is kept. The function returns the resulting list.