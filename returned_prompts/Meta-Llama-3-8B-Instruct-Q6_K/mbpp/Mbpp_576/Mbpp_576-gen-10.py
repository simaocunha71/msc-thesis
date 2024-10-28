```
def is_Sub_Array(arr, sub_arr):
    return all(i in arr for i in sub_arr)
```
The function `is_Sub_Array` checks if all elements of the sublist `sub_arr` are present in the main list `arr`. It uses the built-in function `all` along with a generator expression to check this. The `all` function returns `True` if all elements of the iterable are true, and `False` otherwise. The generator expression `i in arr for i in sub_arr` checks if each element `i` in the sublist is present in the main list. If all elements are present, the function returns `True`, otherwise it returns `False`. 

The unit test `assert is_Sub_Array([1,4,3,5],[1,2]) == False` ensures that the function correctly returns `False` when the sublist is not a sublist of the main list. This is because the sublist `[1,2]` contains elements that are not present in the main list `[1,4,3,5]`. 

This solution assumes that the order of elements in the sublist does not matter, i.e., it treats `[1,2,3]` and `[2,1,3]` as the same sublist. If the order of elements in the sublist does matter, the problem becomes more complex and requires a different solution. 