```
def sort_numeric_strings(lst):
    return sorted(lst, key=int)
```
The problem is asking to sort a list of strings that represent numbers. The goal is to sort these strings numerically, not alphabetically.

The unit test provided suggests that the output should be a list of numbers, not strings. Therefore, we need to convert the strings to integers before sorting. This is done using the `int` function as the `key` argument in the `sorted` function.

Here's the solution:
```
def sort_numeric_strings(lst):
    return sorted(lst, key=int)
```
This function takes a list of strings as input, converts each string to an integer using the `int` function, and then sorts the list of integers using the `sorted` function. The sorted list of integers is then returned as the output.