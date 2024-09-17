```
def big_diff(lst):
    return max(lst) - min(lst)
```
Explanation:
This function uses the built-in Python functions `max()` and `min()` to find the largest and smallest values in the list, respectively. It then subtracts the smallest value from the largest value to find the difference. The unit test `assert big_diff([1,2,3,4]) == 3` ensures that the function is working correctly. 