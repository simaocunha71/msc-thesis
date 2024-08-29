
def reverse_string_list(lst):
    return [s[::-1] for s in lst]


assert reverse_string_list(['Red', 'Green', 'Blue', 'White', 'Black']) == ['deR', 'neerG', 'eulB', 'etihW', 'kcalB']

"""
The function takes a list of strings as input and uses list comprehension to create a new list. For each string in the input list, it uses the [::-1] slice to reverse the string and adds it to the new list. Finally, it returns the new list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3
<jupyter_code>
