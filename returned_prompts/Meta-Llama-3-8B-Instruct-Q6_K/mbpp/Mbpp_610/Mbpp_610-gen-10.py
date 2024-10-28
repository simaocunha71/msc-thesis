```
def remove_kth_element(lst, k):
    if k > len(lst):
        return lst
    return lst[:k-1] + lst[k:]
```


The function `remove_kth_element` takes a list `lst` and an integer `k` as input. It returns a new list with the same elements as `lst`, but the `k'th` element is removed. If `k` is greater than the length of `lst`, the function returns the original list unchanged.

The function works by using Python's list slicing feature. The expression `lst[:k-1]` returns a new list containing all elements of `lst` up to and excluding the `k'th` element. The expression `lst[k:]` returns a new list containing all elements of `lst` starting from the `k'th` element to the end of the list. By concatenating these two lists with the `+` operator, we effectively remove the `k'th` element from the original list.

The unit test `assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]` checks that the function correctly removes the 3rd element from the list `[1,1,2,3,4,4,5,1]`. The expected output is `[1, 1, 3, 4, 4, 5, 1]`, which is the original list with the 3rd element removed. The unit test passes if the function returns the correct output.