```
def second_smallest(lst):
    if len(lst) < 2:
        raise ValueError("List must contain at least two elements")
    lst.sort()
    return lst[1]
```
This function first checks if the list has at least two elements. If not, it raises a ValueError. Then it sorts the list. The second smallest number is the second element in the sorted list, which is at index 1. The function returns this value.

The unit test `assert second_smallest([1, 2, -8, -2, 0, -2])==-2` ensures that the function works correctly by checking that it returns the correct value for a given input. 

Note that this function assumes that the list contains at least one positive number. If the list contains no positive numbers, it will return the second smallest negative number. If you want the function to return the smallest positive number if the list contains no positive numbers, you would need to add additional code to handle this case. 





