Here are two ways of achieving this:

1. Using a while loop:

```python
def move_zero(lst):
    i = 0
    while i < len(lst):
        if lst[i] != 0:
            lst[i], lst[i + (len(lst) - i - 1)] = lst[i + (len(lst) - i - 1)], lst[i]
            i += 1
    return lst
```

2. Using two-pointer technique:

```python
def move_zero(lst):
    left, right = 0, 0
    while right < len(lst):
        if lst[right] != 0:
            lst[left], lst[right] = lst[right], lst[left]
            left += 1
        right += 1
    return lst
```

Both functions will return the list with all zeroes moved to the end: `[1, 2, 3, 4, 0, 0]`

In the first function, we are using a while loop to iterate over the list. If the current element is not a zero, we swap it with the last element of the non-zero part of the list and move to the next element. In the second function, we are using a two-pointer technique. The left pointer starts from the beginning of the list, the right pointer starts from the beginning of the non-zero part of the list. We are swapping the current element with the last element of the non-zero part of the list and move the pointers to the next elements.

Both functions have a time complexity of O(n), where n is the length of the list.

Here are some test cases to validate the function:

```python
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([0,0,0,0]) == [0,0,0,0]
assert move_zero([1,2,3,4,5,6,7,8,9,0,0,0,0]) == [1,2,3