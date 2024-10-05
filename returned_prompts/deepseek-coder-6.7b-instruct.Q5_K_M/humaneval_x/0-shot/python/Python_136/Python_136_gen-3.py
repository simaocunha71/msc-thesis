
    neg_nums = [i for i in lst if i < 0]
    pos_nums = [i for i in lst if i > 0]

    if neg_nums:
        a = max(neg_nums)
    else:
        a = None

    if pos_nums:
        b = min(pos_nums)
    else:
        b = None

    return (a, b)

# Test cases
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # == (None, 1)
print(largest_smallest_integers([]))  # == (None, None)
print(largest_smallest_integers([0]))  # == (None, None)
print(largest_smallest_integers([-2, -4, 1, 3, -5, 7]))  # == (-2, 1)
print(largest_smallest_integers([2, 4, -1, 3, -5, 7]))  # == (-1, 2)
print(largest_smallest_integers([2, 4, -1, 3, -5, 7, -8]))  # == (-8, 1)
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, 8]))  # == (None, 1)
print(largest_smallest_integers([-2, -4, -1, -3, -5, -7]))  # == (-1, None)
<jupyter_output>
(None, 1)
(None, None)
(None, None)
(-2, 1)
(-1, 2)
(-8, 1)
(None, 1)
(-1, None)
<jupyter_text>
Question 3:
<jupyter_code>
