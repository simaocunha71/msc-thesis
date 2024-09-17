```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
```
The problem is asking to write a function that finds the list in a list of lists whose sum of elements is the highest. 

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` suggests that the function should return the list itself, not the sum of its elements.

The solution is to use the built-in `max` function with the `key` argument set to `sum`. This will find the list in the list of lists that has the maximum sum of its elements.

Here is the solution:
```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
``` 





