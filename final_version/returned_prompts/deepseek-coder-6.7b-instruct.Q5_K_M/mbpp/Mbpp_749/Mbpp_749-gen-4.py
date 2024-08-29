def sort_numeric_strings(lst):
    return sorted(map(int, lst))

assert sort_numeric_strings(  ['4','12','45','7','0','100','200','-12','-500'])==[-500, -12, 0, 4, 7, 12, 45, 100, 200]

"""
Here, the map function is used to convert all the strings in the list to integers. Then, sorted function is used to sort these integers in ascending order. The result is a sorted list of integers.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
