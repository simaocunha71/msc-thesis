def max_difference(lst):
    max_diff = 0
    for tup in lst:
        diff = abs(tup[0] - tup[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

assert max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]) == 7
"""
Explanation:
The maximum difference is between (10, 3) which is 7.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Problem 4:
<jupyter_code>
