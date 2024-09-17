You can solve this problem by first calculating the sum of each sublist and then selecting the sublist with the highest sum. Here is a Python function that does this:

```
def max_sum_list(list_of_lists):
    return max(list_of_lists, key=sum)
```

This function uses the built-in `max` function with a `key` argument set to `sum`. This tells `max` to use the sum of each sublist as the value to compare. The sublist with the highest sum will be returned. 

For example, if you call `max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])`, it will return `[10, 11, 12]`, which has the highest sum. 

The unit test `assert max_sum_list([[1,2,3], [4,5,6], [10,11,12], [7,8,9]])==[10, 11, 12]` also passes, as expected. 





This solution assumes that the input list is not empty. If the input list could be empty, you might want to add a check for this before calling `max`. For example:

```
def max_sum_list(list_of_lists):
    if not list_of_lists:
        return []
    return max(list_of_lists, key=sum)
```

This version of the function will return an empty list if the input list is empty, rather than raising an exception. 