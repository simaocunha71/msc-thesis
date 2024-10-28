```
def recursive_list_sum(lst):
    if not lst:
        return 0
    if isinstance(lst[0], list):
        return lst[0][0] + recursive_list_sum(lst[0][1:]) + recursive_list_sum(lst[1:])
    else:
        return lst[0] + recursive_list_sum(lst[1:])
```





I hope it is correct. It works by recursively calling itself on sublists and adding the elements together. If the first element of the list is a sublist, it calls itself on that sublist, then adds the first element of the sublist and the rest of the list. If the first element is not a sublist, it just adds that element to the sum of the rest of the list.

This function passes the given unit test:

```
assert recursive_list_sum(([1, 2, [3,4],[5,6]]))==21
```





Please let me know if you have any questions or need further clarification.