def consecutive_duplicates(lst):
    return [lst[i] for i in range(len(lst)) if i == 0 or lst[i] != lst[i-1]]

assert consecutive_duplicates([0, 0, 1, 2, 3, 4, 4, 5, 6, 6, 6, 7, 8, 9, 4, 4 ])==[0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 4]

"""
Explanation: 
The function works by iterating over the list and only adding an element to the new list if it is not equal to the previous element. 
This effectively removes all consecutive duplicates.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
2.
<jupyter_code>
