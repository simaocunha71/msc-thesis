```
def consecutive_duplicates(lst):
    result = []
    for num in lst:
        if not result or num != result[-1]:
            result.append(num)
    return result
```


This function iterates over the input list and checks if the current number is different from the last number in the result list. If it is, the current number is added to the result list. This effectively removes consecutive duplicates from the list. The unit test provided in the problem description ensures that this function works correctly. For example, the test case `assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]` checks that the function correctly removes consecutive duplicates from the list.