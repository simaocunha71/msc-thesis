```
def smallest_num(lst):
    return min(lst)
```
The min() function in Python returns the smallest item in an iterable or the smallest of two or more arguments. In this case, we are passing the list to the min() function to find the smallest number in the list. 

The unit test `assert smallest_num([10, 20, 1, 45, 99]) == 1` ensures that the function is working correctly by checking if the smallest number in the list is indeed 1. 

This function will work for any list of numbers, not just the one provided in the unit test. It will return the smallest number in the list. 