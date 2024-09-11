Here's a Python function that swaps the first and last elements of a list:

```python
def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        return lst[len(lst) - 1:] + lst[:len(lst) - 1]
```

To test the function, you can use the `assert` statement as follows:

```python
def test_swap_List():
    assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
    print("All tests passed")

test_swap_List()
```

In this test function, the `swap_List` function is called with a sample list `[12, 35, 9, 56, 24]` and the result is compared with the expected output `[24, 35, 9, 56, 12]`. If the result matches the expected output, it prints "All tests passed". Otherwise, it indicates a failure in the test.

By running this code, you can verify if the `swap_List` function correctly interchanges the first and last elements in a list.

```python
def swap_List(lst):
    if len(lst) < 2:
        return lst
    else:
        return lst[len(lst) - 1:] + lst[:len(lst) - 1]
```

This function first checks if the length of the list is less than 2. If so, it means the list has only one or zero elements, and there is no need to swap the first and last elements. In this case, the function simply returns the list as it is.

If the length of the list is 2 or more, the function proceeds to swap the first and last elements. It uses list slicing to create two new lists: one containing the last element of the original list (`lst[len(lst) - 1:]`), and another containing all the elements from the beginning of the original list up to the second-to-last element (`lst[:len