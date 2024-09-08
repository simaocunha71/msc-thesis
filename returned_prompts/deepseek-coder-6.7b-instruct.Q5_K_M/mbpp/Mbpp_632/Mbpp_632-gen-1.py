
def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

"""
Here, first we are creating a list of elements in the original list that are not zero. Then we are creating another list of elements in the original list that are zero. We then concatenate these two lists to get the desired result.
"""
<jupyter_output>
[1, 2, 3, 4, 0, 0]
<jupyter_text>
Question 2:
<jupyter_code>
