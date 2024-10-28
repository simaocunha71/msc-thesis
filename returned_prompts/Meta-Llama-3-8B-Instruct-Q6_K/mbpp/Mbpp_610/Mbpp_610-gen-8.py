```
def remove_kth_element(lst, k):
    return lst[:k-1] + lst[k:]
```


Explanation: 
The function `remove_kth_element` takes a list `lst` and an integer `k` as input. It returns a new list that is the same as the input list, but with the `k`th element removed.

The unit test provided, `assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]`, helps to understand the expected behavior of the function. It shows that the 3rd element (index 2) should be removed from the list.

To solve this problem, we can use Python's list slicing feature. The expression `lst[:k-1]` returns a new list that contains all elements of `lst` up to (but not including) the `k`th element. The expression `lst[k:]` returns a new list that contains all elements of `lst` starting from the `k`th element to the end of the list. By concatenating these two lists, we get a new list that is the same as the input list, but with the `k`th element removed.

For example, if we call `remove_kth_element([1,1,2,3,4,4,5,1],3)`, the function will return `[1, 1, 3, 4, 4, 5, 1]`, which is the input list with the 3rd element removed.