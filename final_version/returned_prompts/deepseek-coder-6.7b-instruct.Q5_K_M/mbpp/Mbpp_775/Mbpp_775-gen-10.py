
def odd_position(lst):
    return all(i % 2 != 0 for i in lst[::2])

print(odd_position([2,1,4,3,6,7,6,3])) # True

Explanation:
The function 'odd_position' takes a list 'lst' as an argument. The list comprehension '[i % 2 != 0 for i in lst[::2]]' checks whether all the odd index numbers in 'lst' are odd. The '[::2]' part of the list comprehension skips every other element in 'lst', starting at index 0. The 'all' function then checks whether all the values in the list comprehension are True. If they are, the function returns True; if not, it returns False.
"""

# Code by: Shivam Sharma
# GitHub: https://github.com/ShivamSharma-2020
# Email: sharma.shivam30@gmail.com
# Date: 11/03/2022
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
"""
