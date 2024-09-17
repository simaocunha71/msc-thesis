```
def extract_nth_element(tuples_list, n):
    if n >= len(tuples_list):
        return []
    return [x for i, x in enumerate(tuples_list) if i == n]
```
This function takes a list of tuples and an integer n as input, and returns the nth element from the list. The function uses list comprehension to iterate over the list and return the nth element. If n is greater than or equal to the length of the list, the function returns an empty list. The unit test `assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']` checks if the function returns the correct nth element. 

Note: The function returns the nth element as a list of tuples, not as a single tuple. If you want to return a single tuple, you can modify the function to return `tuples_list[n]` instead of `[x for i, x in enumerate(tuples_list) if i == n]`. However, this will raise an IndexError if n is out of range. The current implementation returns an empty list in this case. 

Also, the function returns all elements if n is out of range, not just the nth element. If you want to return only the nth element, you can modify the function to return `[tuples_list[n]]` instead of `[x for i, x in enumerate(tuples_list) if i == n]`. However, this will also raise an IndexError if n is out of range. The current implementation returns an empty list in this case. 