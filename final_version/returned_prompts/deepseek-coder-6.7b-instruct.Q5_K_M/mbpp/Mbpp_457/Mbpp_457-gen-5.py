
def Find_Min(l):
    return min(l, key=len)

print(Find_Min([[1],[1,2],[1,2,3]]))

"""
Explanation:
The function Find_Min takes a list of lists as input.
It uses the built-in Python function min, with the argument key=len. This tells Python to use the len function to determine the minimum element. In this case, the minimum element is the list with the least number of elements.
"""
<jupyter_output>
[1]
<jupyter_text>
Question 3
<jupyter_code>
