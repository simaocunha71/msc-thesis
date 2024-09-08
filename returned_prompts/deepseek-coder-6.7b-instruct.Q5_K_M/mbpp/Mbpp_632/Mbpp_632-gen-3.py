def move_zero(lst):
    return [i for i in lst if i != 0] + [i for i in lst if i == 0]

print(move_zero([1,0,2,0,3,4]))

"""
This function works by creating two lists: one for the non-zero elements and one for the zero elements. 
It then concatenates these lists in the order we want.
"""

# Test
assert move_zero([1,0,2,0,3,4]) == [1,2,3,4,0,0]
assert move_zero([0,0,0,0,0,0]) == [0,0,0,0,0,0]
assert move_zero([1,2,3,4,5,6]) == [1,2,3,4,5,6]
assert move_zero([0,1,0,2,0,3,0,4]) == [1,2,3,4,0,0,0,0]
assert move_zero([0,1,0,2,3,0,4,0,5,0]) == [1,2,3,4,5,0,0,0,0,0]
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
