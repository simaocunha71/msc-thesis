
    neg_nums = [num for num in lst if num < 0]
    pos_nums = [num for num in lst if num > 0]

    if not neg_nums:
        largest_neg = None
    else:
        largest_neg = max(neg_nums)

    if not pos_nums:
        smallest_pos = None
    else:
        smallest_pos = min(pos_nums)

    return (largest_neg, smallest_pos)

print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  # (None, 1)
print(largest_smallest_integers([]))  # (None, None)
print(largest_smallest_integers([0]))  # (None, None)

This function works by first creating two lists: neg_nums for negative numbers and pos_nums for positive numbers. Then it finds the maximum of the neg_nums if there are any, otherwise it returns None. It does the same for pos_nums, returning the smallest positive integer or None if there are no positive integers. The function returns a tuple of these two values.
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4: Given a list of integers, write a Python function that computes the average of all the integers in the list.
<jupyter_code>
