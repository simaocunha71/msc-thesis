The problem asks to find the maximum value in a given heterogeneous list. However, it's important to note that the problem doesn't specify the type of values in the list. 

Thanks to the unit test `assert max_val(['Python', 3, 2, 4, 5, 'version'])==5`, we can assume that the maximum value is the largest integer in the list. In this case, the function should return the maximum integer.

Here is the solution:

```Python
def max_val(lst):
    return max([x for x in lst if isinstance(x, int)])
```

This function uses a list comprehension to create a list of integers from the input list. Then, it uses the built-in `max` function to find the maximum value in this list. If the input list is empty, the function will return `None`. If the input list doesn't contain any integers, the function will return `None`. 

Please note that this solution assumes that the input list contains at least one integer. If the input list can be empty or not contain any integers, you should add error handling code to handle these cases. 

For example, you can add a check to see if the list is empty before trying to find the maximum value:

```Python
def max_val(lst):
    if not lst:
        return None
    return max([x for x in lst if isinstance(x, int)])
``` 

Similarly, you can add a check to see if the list contains at least one integer before trying to find the maximum value:

```Python
def max_val(lst):
    integers = [x for x in lst if isinstance(x, int)]
    if not integers:
        return None
    return max(integers)
``` 