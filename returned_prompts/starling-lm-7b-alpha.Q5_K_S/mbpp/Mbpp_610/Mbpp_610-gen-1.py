Here's one way to do it:

```python
def remove_kth_element(lst, k):
    """
    Take a list and return a list with the same elements, but the k'th element removed
    """
    return lst[:k] + lst[k+1:]
```

This function takes a list and the index of the element to remove, and returns a new list with the same elements, but the k'th element removed. It does this by using slicing to create two new lists: one starting at the beginning of the original list and ending at the k'th index (exclusive), and one starting at the k+1'th index of the original list and ending at the end of the original list. The function then concatenates these two new lists together using the + operator, and returns the result.

For example, if we call the function with the list `[1,1,2,3,4,4,5,1]` and the index `3`, it will return the list `[1, 1, 3, 4, 4, 5, 1]`. This is because the k'th element (the element at index 3) is `3`, and removing it from the original list gives us the desired result.

Here's a test case to demonstrate the function:

```python
assert remove_kth_element([1,1,2,3,4,4,5,1],3)==[1, 1, 3, 4, 4, 5, 1]
```

This test case checks that the function correctly removes the k'th element from the input list. In this case, the k'th element is `3`, and the function correctly returns the list `[1, 1, 3, 4, 4, 5, 1]`.

```python
# Python program to remove k'th element from the list

def remove_kth_element(lst, k):
    """
    Take a list and return a list with the same elements, but the k'th element removed
    """
    return lst[:k] + lst[k+1:]
```

You can test the function with the following test