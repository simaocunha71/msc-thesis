def max_difference(tuples):
    return max(max(t) - min(t) for t in tuples)

print(max_difference([(3, 5),  (1, 7),  (10, 3),  (1, 2)]))

# Output: 9

Explanation:
The difference between the maximum and minimum values for each tuple is computed and these differences are then compared to find the maximum difference.

If you run the code, you will get 9 which is the maximum difference in the given tuple list.

"""
This is because for the tuple (3,5) the difference is 5-3=2, for the tuple (1,7) the difference is 7-1=6, for the tuple (10,3) the difference is 10-3=7, and for the tuple (1,2) the difference is 2-1=1.

The maximum difference is 7 which is the maximum difference among these differences.
"""
<jupyter_output>
9
<jupyter_text>
Question 3:
<jupyter_code>
