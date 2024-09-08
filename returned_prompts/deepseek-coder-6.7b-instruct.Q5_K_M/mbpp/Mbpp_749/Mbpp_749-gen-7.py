def sort_numeric_strings(lst):
    return sorted(int(num) for num in lst)

print(sort_numeric_strings( ['4','12','45','7','0','100','200','-12','-500']))

"""
Output:
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
"""

"""
Explanation:

The function `sort_numeric_strings` takes a list of string numbers as an argument. It uses a generator expression to convert each string in the list to an integer, which is then passed to the `sorted` function to sort the numbers in ascending order. The result is a new list with the numbers sorted numerically.

The `int` function is used to convert the strings to integers. The `sorted` function is then used to sort the integers.
"""
<jupyter_output>
[-500, -12, 0, 4, 7, 12, 45, 100, 200]
<jupyter_text>
Question 2
<jupyter_code>
