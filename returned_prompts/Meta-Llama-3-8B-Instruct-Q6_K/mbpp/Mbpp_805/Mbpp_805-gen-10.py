```
def max_sum_list(lists):
    max_sum = 0
    max_list = None
    for lst in lists:
        if sum(lst) > max_sum:
            max_sum = sum(lst)
            max_list = lst
    return max_list
```





This function iterates over each list in the input list of lists. For each list, it calculates the sum of its elements. If the sum of the current list is greater than the maximum sum found so far, it updates the maximum sum and the corresponding list. Finally, it returns the list with the maximum sum.

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` helps to clarify that the function should return the entire list with the highest sum, not just the sum itself. This is why the function returns `max_list` instead of `max_sum`.