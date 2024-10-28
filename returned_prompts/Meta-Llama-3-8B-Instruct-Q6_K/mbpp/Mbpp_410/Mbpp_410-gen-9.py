The problem is asking to create a function that finds the minimum value in a given list. However, the problem doesn't specify the type of values in the list. 

Fortunately, the unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2` gives us a hint. It suggests that the list can contain any type of values, and the function should return the smallest integer value. This is a reasonable assumption because the problem statement doesn't specify what type of value is being sought.

Here's a Python solution for the problem:

```
def min_val(lst):
    return min(x for x in lst if isinstance(x, int))
```

This function uses a generator expression to iterate over the list, and the `isinstance` function to check if each element is an integer. The `min` function then returns the smallest integer value in the list. If the list is empty or doesn't contain any integers, the function will raise a ValueError. If you want to handle these cases differently, you can add additional error checking code. 





Note: This solution assumes that the list contains at least one integer. If the list is empty or doesn't contain any integers, the function will raise a ValueError. If you want to handle these cases differently, you can add additional error checking code.