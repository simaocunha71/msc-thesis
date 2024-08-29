def sort_numeric_strings(lst):
    return sorted(int(num) for num in lst)

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))

# Output: [-500, -12, 0, 4, 7, 12, 45, 100, 200]

"""
In this function, we use a generator expression to convert each string to an integer. Then we pass this to the sorted function which returns a new sorted list.
"""
<jupyter_output>
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<jupyter_text>
