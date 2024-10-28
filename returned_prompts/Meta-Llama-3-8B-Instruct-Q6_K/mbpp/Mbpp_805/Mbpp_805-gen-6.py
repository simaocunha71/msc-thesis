The problem is asking to create a function that finds the list in a list of lists with the highest sum of its elements. 

However, the problem description does not specify what to do if there are multiple lists with the same highest sum. 

Fortunately, the unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` provides a clue. It suggests that the function should return the first list it encounters with the highest sum. 

Here is a Python solution for the problem:

```
def max_sum_list(lists):
    max_sum = float('-inf')
    max_list = []
    for lst in lists:
        total = sum(lst)
        if total > max_sum:
            max_sum = total
            max_list = lst
    return max_list
```

This function iterates over each list in the input list of lists. For each list, it calculates the sum of its elements. If the sum is greater than the current maximum sum, it updates the maximum sum and the corresponding list. Finally, it returns the list with the highest sum. 

Note that this function returns the first list with the highest sum, as per the unit test. If there are multiple lists with the same highest sum, it will return the first one it encounters.  If you want to return all lists with the highest sum, you would need to modify the function to keep track of all lists with the maximum sum, not just the first one. 