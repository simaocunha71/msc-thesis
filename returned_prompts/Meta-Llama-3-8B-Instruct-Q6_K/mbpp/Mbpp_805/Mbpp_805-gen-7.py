```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key = sum)
```





The problem asks to write a function that takes a list of lists as input and returns the list in that list of lists whose sum of elements is the highest.

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` helps to understand the problem better.

The solution is to use the built-in `max` function in Python with the `key` argument set to `sum`. This function returns the item with the highest sum of its elements. 

Here is the Python function that solves the problem:

```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key = sum)
```





This function takes a list of lists as input, and returns the list in that list of lists whose sum of elements is the highest. The `max` function is used with the `key` argument set to `sum`, which tells the function to compare the lists based on the sum of their elements. The function returns the list with the highest sum of elements.