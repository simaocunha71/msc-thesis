def sort_numeric_strings(lst):
    return sorted(int(i) for i in lst)

assert sort_numeric_strings(['4', '12', '45', '7', '0', '100', '200', '-12', '-500']) == [-500, -12, 0, 4, 7, 12, 45, 100, 200]

"""
The function sorts the list of strings by converting each string to an integer and then sorting the resulting list of integers.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
