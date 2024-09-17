```
def check_Consecutive(lst):
    if len(lst) < 2:
        return False
    for i in range(len(lst)-1):
        if lst[i+1] - lst[i] != 1:
            return False
    return True
```


This function checks if the list contains consecutive numbers. It first checks if the list has at least two elements. If not, it returns False, as there cannot be consecutive numbers in a list with less than two elements.

Then it iterates over the list, checking if the difference between the current element and the next element is 1. If it finds an element where the difference is not 1, it returns False, as that means the list does not contain consecutive numbers.

If the function does not find any non-consecutive elements, it returns True, indicating that the list contains consecutive numbers. The unit test `assert check_Consecutive([1,2,3,4,5]) == True` confirms that this function works correctly. 





