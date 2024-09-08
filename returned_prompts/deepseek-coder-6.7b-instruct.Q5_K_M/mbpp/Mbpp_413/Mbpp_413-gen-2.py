def extract_nth_element(lst, n):
    return [i[n] for i in lst]

print(extract_nth_element([('Greyson Fulton', 98, 99), 
                           ('Brady Kent', 97, 96), 
                           ('Wyatt Knott', 91, 94), 
                           ('Beau Turnbull', 94, 98)],0))

"""
Output: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
"""

"""
Explanation:
In the function 'extract_nth_element', we are given a list of tuples and an integer 'n'. We are to extract the nth element from each tuple in the list and return a new list containing these extracted elements. 

We achieve this by using a list comprehension. For each tuple 'i' in the list 'lst', we take the nth element 'i[n]' and append it to the new list.

In the sample question, the value of 'n' is 0, which means we want to extract the first element of each tuple. The output is a list containing these first elements ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'].
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 2
<jupyter_code>
