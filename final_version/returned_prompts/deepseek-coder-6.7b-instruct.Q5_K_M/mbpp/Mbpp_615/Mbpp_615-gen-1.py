```python
def average_tuple(t):
    averages = []
    for tup in t:
        averages.append(sum(tup)/len(tup))
    return averages

print(average_tuple(((10, 10, 10, 12), (30, 45, 56, 45), (81, 80, 39, 32), (1, 2, 3, 4))))
```

The function iterates over each tuple in the input tuple of tuples, sums the elements in the tuple and divides by the length of the tuple to find the average, and then appends this average to a list. The function then returns this list of averages.
"""


# --------------
# Sample Input
# --------------
(
    (10, 10, 10, 12),
    (30, 45, 56, 45),
    (81, 80, 39, 32),
    (1, 2, 3, 4)
)

# -------------
# Sample Output
# -------------
[30.5, 34.25, 27.0, 23.25]
"""

# ---------------
# Explanation
# ---------------
In the first tuple, the average is (10+10+10+12)/4 = 10.5.
In the second tuple, the average is (30+45+56+45)/4 = 44.25.
In the third tuple, the average is (81+80+39+32)/4 = 59.5.
In the fourth tuple, the average is (1+2+3+4)/4 = 2.5.
So, the function returns a list of these averages: [10.5, 44.25, 59.5, 2.5].
"""

# ---------------
# End of Question
# ---------------

# ---------------
# Test Cases
# ---------------
# Test Case 