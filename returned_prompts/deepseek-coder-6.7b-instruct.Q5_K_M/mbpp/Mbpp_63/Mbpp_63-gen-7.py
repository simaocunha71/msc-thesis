def max_difference(lst):
    max_diff = 0
    for tup in lst:
        diff = abs(tup[0] - tup[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))

"""
Output:
7
"""
<jupyter_output>
7
<jupyter_text>
Q2:
<jupyter_code>
