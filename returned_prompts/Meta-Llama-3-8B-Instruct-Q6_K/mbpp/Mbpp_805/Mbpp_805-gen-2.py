You can solve this problem by using the built-in function max() along with a lambda function to find the maximum list in the list of lists based on the sum of its elements.

Here is the Python solution:

```Python
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
```

This function works by iterating over each list in the list of lists, calculating the sum of its elements, and then returning the list with the maximum sum. The built-in function max() is used to find the maximum list, and the key argument is set to the sum function to specify that the maximum list should be the one with the highest sum. 

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` demonstrates the functionality of the function. It checks if the function returns the list `[10, 11, 12]`, which is the list with the highest sum in the list of lists. 

The function is flexible and can be used with any list of lists, not just the one provided in the unit test. It will always return the list with the highest sum, regardless of the actual values in the list. 





