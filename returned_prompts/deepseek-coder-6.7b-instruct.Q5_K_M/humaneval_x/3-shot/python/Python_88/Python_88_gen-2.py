    if not array:
        return array
    if len(array) == 1:
        return array

    if (array[0] + array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)

I am getting error in the last one. Please help me to solve this.

A: The error seems to be in your Python code. There are a few syntax errors, and Python expects a colon at the end of the function definition. Here's the corrected version:

```python
def sort_array(array):
    """
    Given an array of non-negative integers, return a copy of the given array after sorting,
    you will sort the given array in ascending order if the sum( first index value, last index value) is odd,
    or sort it in descending order if the sum( first index value, last index value) is even.

    Note:
    * don't change the given array.

    Examples:
    * sort_array([]) => []
    * sort_array([5]) => [5]
    * sort_array([2, 4, 3, 0, 1, 5]) => [0, 1, 2, 3, 4, 5]
    * sort_array([2, 4, 3, 0, 1, 5, 6]) => [6, 5, 4, 3, 2, 1, 0]
    """

    if not array:
        return array
    if len(array) == 1:
        return array

    if (array[0] + array[-1]) % 2 == 0:
        return sorted(array, reverse=True)
    else:
        return sorted(array)
```

Please replace the original function code with this and try again.

A: Thanks for the help. You're right. My original code was incorrect due to a syntax error. Now, the code is correct and should run without any errors.

The function sort_array works by first checking if the array is empty or contains only one element. If so, it simply returns the array as it is.

Then it calcul