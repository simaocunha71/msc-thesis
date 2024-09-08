def find_dissimilar(t1, t2):
    return tuple(set(t1) ^ set(t2))

print(find_dissimilar((3, 4, 5, 6), (5, 7, 4, 10)))

# set() function is used to convert the tuple to a set.
# ^ operator is used to find the symmetric difference of two sets.
# tuple() function is used to convert the set back to a tuple.

"""
Output:
(3, 6, 7, 10)
"""
<jupyter_output>
<empty_output>
<jupyter_text>
**Question 2:**
<jupyter_code>
