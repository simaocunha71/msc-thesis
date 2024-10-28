```
def issort_list(lst):
    return all(lst[i] <= lst[i+1] for i in range(len(lst)-1))
```





The function `issort_list` takes a list `lst` as input. It uses the `all` function along with a generator expression to check if all elements in the list are in sorted order.

The generator expression `lst[i] <= lst[i+1] for i in range(len(lst)-1)` compares each element in the list with the next element. If all elements are in sorted order, the `all` function returns `True`; otherwise, it returns `False`.

The unit test `assert issort_list([1,2,4,6,8,10,12,14,16,17])==True` ensures that the function correctly identifies a sorted list.