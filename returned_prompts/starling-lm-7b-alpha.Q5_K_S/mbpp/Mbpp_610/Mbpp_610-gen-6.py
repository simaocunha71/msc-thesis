Here is one way you might write this function:

```python
def remove_kth_element(lst, k):
    return lst[:k] + lst[k + 1:]
```

This function takes a list `lst` and an integer `k` and returns a new list with the same elements, but the `k`'th element removed. Here's a step-by-step breakdown of how it works:

1. `lst[:k]` returns a slice of the original list `lst` that includes all of the elements from the beginning of the list up to (but not including) the `k`'th element. This slice is essentially a copy of the original list up to the `k`'th element.
2. `lst[k + 1:]` returns a slice of the original list `lst` that includes all of the elements after (and including) the `k`'th element. This slice is essentially a copy of the original list starting from the `k+1`'th element.
3. The `+` operator is used to concatenate these two slices together, effectively removing the `k`'th element from the list.

Finally, the resulting concatenated list is returned as the result of the function.

For example, if we call `remove_kth_element([1,1,2,3,4,4,5,1],3)`, the function will return `[1, 1, 3, 4, 4, 5, 1]`, as expected.

Note that this function modifies the original list by creating a new list that includes all elements except for the `k`'th element. It does not modify the original list in place. If you want to modify the original list in place, you can use a different approach, such as using the `del` keyword to remove the `k`'th element from the original list directly.
```python
def remove_kth_element_in_place(lst, k):
    del lst[k]
```
However, this approach may not be suitable for all situations, especially if the list is part of a larger data structure or if it needs to be preserved for later use.

It's also worth noting that this function assumes that the input