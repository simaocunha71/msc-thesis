
def extract_nth_element(lst,n):
    return [i[n] for i in lst]

print(extract_nth_element([('Greyson Fulton', 98, 99), 
                           ('Brady Kent', 97, 96), 
                           ('Wyatt Knott', 91, 94), 
                           ('Beau Turnbull', 94, 98)],0))
<jupyter_output>
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
<jupyter_text>
Question 3
<jupyter_code>
