
def sum_negativenum(lst):
    return sum(i for i in lst if i < 0)

print(sum_negativenum([2, 4, -6, -9, 11, -12, 14, -5, 17]))

"""
The function sum_negativenum takes a list lst as an argument and returns the sum of all the negative numbers in the list.
We use a generator expression inside the sum() function to create a sequence of all the negative numbers in the list, then sum() adds them up.
"""

# Output: -32
<jupyter_output>
-32
<jupyter_text>
Question 2:
<jupyter_code>
