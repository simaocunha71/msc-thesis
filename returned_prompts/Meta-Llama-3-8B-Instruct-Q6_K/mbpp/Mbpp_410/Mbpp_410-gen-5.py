The problem asks to create a function that finds the minimum value in a given list. However, the list can contain different types of data, not just numbers. 

The unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2` suggests that we need to find the smallest number in the list. 

Here's a Python solution for this problem:

```
def min_val(lst):
    return min(num for num in lst if isinstance(num, (int, float)))
```

This function uses a generator expression to iterate over the list, filter out non-numeric values using the `isinstance` function, and then find the minimum value using the built-in `min` function. 

Note that this solution assumes that the list is not empty and contains at least one numeric value. If the list can be empty or contain no numeric values, you may want to add error handling to handle these cases.  For example:

```
def min_val(lst):
    num_list = [num for num in lst if isinstance(num, (int, float))]
    if num_list:
        return min(num_list)
    else:
        return None  # or some other default value
``` 