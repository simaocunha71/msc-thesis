def swap_List(lst):
    # store the first element in a variable
    first_element = lst[0]
    
    # store the last element in a variable
    last_element = lst[-1]
    
    # replace the first element with the last element
    lst[0] = last_element
    
    # replace the last element with the first element
    lst[-1] = first_element
    
    return lst

assert swap_List([12, 35, 9, 56, 24]) == [24, 35, 9, 56, 12]
"""
In the above code:
- We define a function called swap_List that takes a list as an argument.
- We save the first element of the list in a variable called first_element.
- We save the last element of the list in a variable called last_element.
- We replace the first element of the list with the last element.
- We replace the last element of the list with the first element.
- We return the modified list.
"""
<jupyter_output>
<empty_output>
<jupyter_text>
Question 3:
<jupyter_code>
