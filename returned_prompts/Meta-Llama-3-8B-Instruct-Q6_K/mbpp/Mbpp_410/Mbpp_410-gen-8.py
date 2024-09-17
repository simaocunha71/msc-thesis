The problem is asking to write a function that finds the minimum value in a given heterogeneous list. The list can contain any type of elements, including integers, floats, and strings. 

However, the problem does not specify what to do if the list contains only strings or if the list is empty. 

Luckily, the provided unit test `assert min_val(['Python', 3, 2, 4, 5, 'version'])==2` gives us a hint. It suggests that we need to consider all elements in the list as numbers and return the smallest one. If the list contains only strings, we can return the first string. If the list is empty, we can return a default value.

Here is a Python solution for the problem:

```
def min_val(lst):
    if not lst:
        return float('inf')  # return infinity for empty list
    return min(map(int, filter(str.isdigit, lst))) if any(str.isdigit(x) for x in lst) else min(lst)
```

This function first checks if the list is empty. If it is, it returns infinity. Then it filters the list to only include elements that are strings of digits. It converts these strings to integers and finds the minimum value. If the list does not contain any strings of digits, it simply finds the minimum value in the list. 

This solution assumes that the list does not contain any non-integer, non-string values. If the list can contain such values, the solution needs to be modified to handle them. 

For example, if the list can contain floats, the function should convert them to integers before finding the minimum value. If the list can contain complex numbers, the function should raise an error because complex numbers cannot be compared with integers. 

The function also assumes that the list is not extremely large, because finding the minimum value in a very large list can be inefficient. If the list can be extremely large, the function should use a more efficient algorithm, such as the heap queue algorithm. 