
def max_difference(tuples):
    max_diff = 0
    for t in tuples:
        diff = abs(t[0] - t[1])
        if diff > max_diff:
            max_diff = diff
    return max_diff


print(max_difference([(3, 5),  (1, 7),  (10, 3),  (1, 2)]))  # 7

"""
Explanation: 

The function `max_difference()` takes a list of tuples as an argument.
For each tuple in the list, it calculates the absolute difference between the two numbers.
If this difference is greater than the current maximum difference (`max_diff`), then `max_diff` is updated to this new value.

At the end of the function, `max_diff` contains the maximum difference found in the list of tuples, and this value is returned.
"""
<jupyter_output>
7
<jupyter_text>
Problem 4
<jupyter_code>
