def extract_nth_element(lst, n):
    return [x[n] for x in lst]

print(extract_nth_element([('Greyson Fulton', 98, 99),  ('Brady Kent', 97, 96),  ('Wyatt Knott', 91, 94),  ('Beau Turnbull', 94, 98)],0))

# Output: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

"""
Explanation:
The function `extract_nth_element` takes two arguments: a list of tuples and an integer `n`. It creates a new list by iterating over the original list and adding the nth element of each tuple to the new list. The function returns the new list.
"""
<jupyter_output>
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
<jupyter_text>
