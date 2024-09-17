```
def big_diff(lst):
    return max(lst) - min(lst)
```
Explanation:
The problem is asking to write a function that takes a list of numbers as an input and returns the difference between the largest and smallest values in the list.

The unit test provided, `assert big_diff([1,2,3,4]) == 3`, suggests that the function should return the difference between the largest and smallest values in the list.

The solution uses the built-in `max` and `min` functions in Python to find the largest and smallest values in the list, respectively. The difference between these two values is then returned by the function.

For example, if the input list is `[1,2,3,4]`, the function will return `4-1 = 3`. This is in accordance with the unit test provided. 