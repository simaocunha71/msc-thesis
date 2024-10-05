
    negative_lst = [x for x in lst if x < 0]
    positive_lst = [x for x in lst if x > 0]

    if negative_lst:
        a = max(negative_lst)
    else:
        a = None

    if positive_lst:
        b = min(positive_lst)
    else:
        b = None

    return (a, b)
<jupyter_output>
<empty_output>
<jupyter_text>
Test Cases
<jupyter_code>
print(largest_smallest_integers([2, 4, 1, 3, 5, 7]))  #== (None, 1)
print(largest_smallest_integers([]))  #== (None, None)
print(largest_smallest_integers([0]))  #== (None, None)
print(largest_smallest_integers([-2, -4, -1, -3, -5, 7]))  #== (-1, 7)
print(largest_smallest_integers([2, 4, 1, 3, 5, 7, -2, -4, -1, -3, -5]))  #== (-1, 1)
<jupyter_output>
(None, 1)
(None, None)
(None, None)
(-1, 7)
(-1, 1)
<jupyter_text>
Task 2: Write a Python function to implement a binary search algorithm.
<jupyter_code>
