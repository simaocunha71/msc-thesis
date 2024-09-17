```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```



The provided unit test suggests that the function should return True if the list is sorted and False otherwise. The function uses the built-in `all()` function and a generator expression to check if all elements in the list are in ascending order.

Here's how it works:
- `all()` returns True if all elements of the iterable (in this case, the generator expression) are true.
- The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` checks if each element in the list is less than or equal to the next one. This is done by comparing each element with its successor.
- If the list is sorted, all elements will be less than or equal to their successors, so `all()` will return True. If the list is not sorted, `all()` will return False. 

This function assumes that the list is a list of comparable elements (e.g., numbers, strings, etc.). If the list contains non-comparable elements, the function may not work correctly. 





Note: The unit test provided, `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True`, suggests that the list should be sorted in ascending order. If the list can be sorted in descending order, the function would need to be modified accordingly. 