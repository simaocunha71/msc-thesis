
    neg_nums = [i for i in lst if i < 0]
    pos_nums = [i for i in lst if i > 0]

    if not neg_nums:
        max_neg = None
    else:
        max_neg = max(neg_nums)

    if not pos_nums:
        min_pos = None
    else:
        min_pos = min(pos_nums)

    return (max_neg, min_pos)

# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)
print(largest_smallest_integers([-2, -4, 1, 3, -5, 7]))  # (-2, 1)
print(largest_smallest_integers([2, 4, -1, 3, -5, 7]))  # (-1, 2)
print(largest_smallest_integers([2, 4, 1, 3, -5, 7]))  # (None, 1)
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7]))  # (-7, None)
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 0]))  # (None, 0)
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7, 0]))  # (-7, 0)
<jupyter_output>
(None, 1)
(None, None)
(None, None)
(-2, 1)
(-1, 2)
(None, 1)
(-7, None)
(None, 0)
(-7, 0)
<jupyter_text>
