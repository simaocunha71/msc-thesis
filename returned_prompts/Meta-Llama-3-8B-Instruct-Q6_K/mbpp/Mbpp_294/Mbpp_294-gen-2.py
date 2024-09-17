```
def max_val(lst):
    return max(map(int, [x for x in lst if isinstance(x, int)]))
```
This function uses a list comprehension to create a list of integers from the input list, and then uses the built-in `max` function to find the maximum value in that list.

The `map` function is used to convert each integer in the list to an integer, and the `isinstance` function is used to filter out non-integer values. The `max` function returns the maximum value in the list, which is then returned by the `max_val` function.

The unit test `assert max_val(['Python', 3, 2, 4, 5, 'version'])==5` ensures that the function works correctly. It checks that the maximum value in the list `['Python', 3, 2, 4, 5, 'version']` is indeed `5`.