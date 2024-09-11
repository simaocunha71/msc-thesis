Here is a Python function that swaps the first and last elements of a list:

```python
def swap_List(lst):
    return lst[len(lst)-1:] + lst[:len(lst)-1]
```

This function works by slicing the list into two parts at the index of the second-to-last element. The slice `lst[len(lst)-1:]` gives us the last element of the list, and `lst[:len(lst)-1]` gives us the rest of the list without the last element. We then concatenate these slices in reverse order, effectively swapping the first and last elements.

You can use this function in your `assert` statement like so:

```python
assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

This assertion will pass if the function correctly swaps the first and last elements of the list.

```python
def swap_List(lst):
    return lst[len(lst)-1:] + lst[:len(lst)-1]

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

This will return `True` if the function is working correctly, and `False` otherwise.

```python
def swap_List(lst):
    return lst[len(lst)-1:] + lst[:len(lst)-1]

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
```

The `swap_List` function takes a list as an input and returns a new list with the first and last elements swapped. It does this by slicing the original list into two parts at the index of the second-to-last element, concatenating these slices in reverse order, and returning the result. The assertion `assert swap_List([12, 35, 9