```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```


This function uses the built-in `all` function along with a generator expression to check if all elements in the list are in sorted order. The `all` function returns `True` if all elements of the iterable (in this case, the generator expression) are true. The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` checks if each element in the list is less than or equal to the next element. If any element is not less than or equal to the next element, the function will return `False`. If the function does not return `False`, then all elements in the list are in sorted order, and the function returns `True`. 





This function will return `True` if the list is sorted, and `False` otherwise. It will also work with lists that contain duplicate values, and lists that are already sorted in reverse order. For example, `issort_list([1,2,2,3,4,4,5,6,7,8])` will return `True`, and `issort_list([10,9,8,7,6,5,4,3,2,1])` will also return `True`. 





The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` will pass, because the list `[1,2,4,6,8,10,12,14,16,17]` is sorted in ascending order. 





The function can be used to check the sortedness of any list, not just lists of integers. For example, `issort_list(['apple','banana','cherry'])` will return `True` if the list is sorted alphabetically, and `False` otherwise. 





The function does not modify the original list. It simply checks the sortedness of the list and returns a boolean value indicating whether the list is sorted or not. 





The time complexity of this function is O(n), where n is the length of the list. This is because the function needs to iterate over the entire list to check the sortedness. The space complexity is O(1), because the function only uses a constant amount of space to store the generator expression and the result. 





This function is efficient