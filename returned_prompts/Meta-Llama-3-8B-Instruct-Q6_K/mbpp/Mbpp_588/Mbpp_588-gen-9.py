```
def big_diff(lst):
    return max(lst) - min(lst)
```


The unit test provided is `assert big_diff([1,2,3,4]) == 3`. This test indicates that the function should return the difference between the largest and smallest value in the list. 

The function `big_diff` takes a list as an argument and returns the difference between the maximum and minimum values in the list. This is achieved using the built-in Python functions `max` and `min` to find the maximum and minimum values in the list, and then subtracting the minimum from the maximum. 

For example, if the input list is `[1, 2, 3, 4]`, the function will return `4 - 1 = 3`. This is in line with the expected output from the unit test. 





