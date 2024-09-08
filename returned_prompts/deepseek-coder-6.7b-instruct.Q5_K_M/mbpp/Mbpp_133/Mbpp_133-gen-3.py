def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

# Output: -32

"""
Explanation:
The function `sum_negativenum` takes a list `lst` as an argument. 
It uses a generator to iterate over each element `i` in the list. 
If `i` is less than 0 (i.e., it's a negative number), it includes it in the sum.
Finally, it returns the sum of these negative numbers.
"""

# You can also use list comprehension as below

def sum_negativenum(lst):
    return sum([i for i in lst if i < 0])

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

# Output: -32

# Both methods will give the same output.
<jupyter_output>
-32
-32
<jupyter_text>
**Problem 2**
<jupyter_code>
