You can use the built-in functions min and max to find the smallest and largest values in the list, and then subtract the smallest from the largest to find the difference.

Here is the Python function that does this:

```
def big_diff(lst):
    return max(lst) - min(lst)
```

This function takes a list as an argument, finds the maximum and minimum values in the list using the built-in max and min functions, and then returns the difference between these two values. The unit test `assert big_diff([1,2,3,4]) == 3` ensures that the function works correctly. For example, when called with the list `[1,2,3,4]`, it returns `3`, which is the difference between the largest value `4` and the smallest value `1` in the list. 