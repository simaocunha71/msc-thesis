You can solve this problem with the following function:

```python
def big_diff(lst):
    return max(lst) - min(lst)
``` 

This function works by first finding the maximum value (max) in the list, and then finding the minimum value (min). It then subtracts the minimum from the maximum to give the difference between the largest and smallest values. The unit test `assert big_diff([1,2,3,4]) == 3` ensures that this function works correctly. 

For example, if you call `big_diff([1,2,3,4])`, it will return `3`, which is the difference between the largest value (`4`) and the smallest value (`1`) in the list. 

This function is quite simple and efficient, and it works for lists of any size. It does not require any specific input or error checking, as it will work with any list of numbers. 