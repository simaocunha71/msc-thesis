def sort_numeric_strings(lst):
    return sorted(int(i) for i in lst)

print(sort_numeric_strings(['4','12','45','7','0','100','200','-12','-500']))

# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

"""
Explanation:
The function sort_numeric_strings takes a list of strings as input. 
It converts each string to an integer using a generator expression. 
The sorted function is then used to sort the integers. 
The result is a new list of integers sorted in ascending order. 
The function returns this new list.
"""
<jupyter_output>
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<jupyter_text>
**Question 3**
<jupyter_code>
