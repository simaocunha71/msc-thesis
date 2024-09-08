def rotate_right(lst, k):
    # We use list slicing to rotate the list
    return lst[-k:] + lst[:-k]

print(rotate_right([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3))


# Output: [8, 9, 10, 1, 2, 3, 4, 5, 6, 7]


"""
In the function `rotate_right(lst, k)`, we are taking two slices of the list: `lst[-k:]` and `lst[:-k]`. The `-k` index in the slice notation means that we start from the `k`th element from the end of the list and go till the end of the list. Similarly, `lst[:-k]` means that we start from the beginning of the list and go till the `k`th element from the end of the list. 

The `+` operator then combines these two slices to form the rotated list. The last `k` elements of the original list are put first and followed by the first `k` elements of the original list.
"""
<jupyter_output>
[8, 9, 10, 1, 2, 3, 4, 5, 6, 7]
<jupyter_text>
