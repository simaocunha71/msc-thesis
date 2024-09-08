def extract_nth_element(lst, n):
    return [i[n] for i in lst]

print(extract_nth_element([('Greyson Fulton', 98, 99),  ('Brady Kent', 97, 96),  ('Wyatt Knott', 91, 94),  ('Beau Turnbull', 94, 98)],0))

#Output: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']

#Explanation: The function extract_nth_element takes a list of tuples and an integer n as arguments. It uses a list comprehension to create a new list where each element is the nth element of each tuple in the list. The function then returns this new list.

#The list comprehension iterates over each tuple in the list, and for each tuple, it takes the element at index n and adds it to the new list.

#The assert statement tests the function with the provided test case. If the function returns the expected result, the assert statement does nothing. If the function does not return the expected result, the assert statement raises an AssertionError with a message indicating that the function returned an incorrect result.

#In this case, the function correctly returns the first element from each tuple in the list.
<jupyter_output>
['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']
<jupyter_text>
Question 2
<jupyter_code>
