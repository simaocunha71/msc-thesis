```
def big_diff(lst):
    return max(lst) - min(lst)
```



Explanation:
The problem asks for a function that takes a list of numbers as input and returns the difference between the largest and smallest values in that list.

The unit test provided, `assert big_diff([1,2,3,4]) == 3`, suggests that the function should return the absolute difference between the largest and smallest values, which is a common interpretation of the phrase "difference" in this context.

In Python, we can use the built-in `max` and `min` functions to find the largest and smallest values in the list, respectively. We can then subtract the smallest value from the largest value to get the difference.

Here's the solution:
```
def big_diff(lst):
    return max(lst) - min(lst)
```
This function takes a list `lst` as input, finds the maximum value using `max(lst)`, finds the minimum value using `min(lst)`, and returns the difference between the two using the subtraction operator `-`. The result is the difference between the largest and smallest values in the input list.