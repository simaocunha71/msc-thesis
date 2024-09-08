
def max_difference(tuples):
    diffs = [abs(t[0] - t[1]) for t in tuples]
    return max(diffs)

print(max_difference([(3, 5), (1, 7), (10, 3), (1, 2)]))  # Output: 7

"""
Explanation:
This function works by first creating a list of the absolute differences between the first and second elements of each tuple. It then returns the maximum value in this list.
"""
<jupyter_output>
7
<jupyter_text>
Question 2
<jupyter_code>
