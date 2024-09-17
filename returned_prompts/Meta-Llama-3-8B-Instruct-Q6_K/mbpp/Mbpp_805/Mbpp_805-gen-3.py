You can solve this problem by using a list comprehension and the built-in max function in Python. The max function returns the item with the maximum value. In this case, we want the list with the maximum sum, so we use a lambda function with the sum function as the key for the max function.

Here is the solution:
```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
```
This function takes a list of lists as input and returns the list in the list of lists whose sum of elements is the highest. The key argument of the max function is a function that takes one argument and returns one value. In this case, the key is the sum function, which calculates the sum of the elements in a list. The max function then returns the list with the maximum sum. 

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` ensures that the function works correctly. It checks if the function returns the list `[10, 11, 12]`, which is the list with the highest sum in the input list of lists. If the function returns the correct result, the unit test passes; otherwise, it fails. 