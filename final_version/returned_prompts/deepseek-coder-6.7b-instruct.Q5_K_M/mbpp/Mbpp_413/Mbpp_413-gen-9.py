def extract_nth_element(lst, n):
    return [x[n] for x in lst]
"""
The function extract_nth_element takes a list of tuples and an integer n as arguments.
It returns a new list that contains the nth element from each tuple in the input list.
"""

# Test the function
print(extract_nth_element([('Greyson Fulton', 98, 99), 
                            ('Brady Kent', 97, 96), 
                            ('Wyatt Knott', 91, 94), 
                            ('Beau Turnbull', 94, 98)], 
                           0))
<jupyter_output>
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
<jupyter_text>
**Question 2**
<jupyter_code>
