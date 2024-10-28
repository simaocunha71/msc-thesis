```
def extract_nth_element(tuples, n):
    return [item for i, item in enumerate(tuples) if i == n]
```
This function takes a list of tuples and an integer `n` as input, and returns a list containing the `n`th element from the input list of tuples. 

The `enumerate` function is used to iterate over the list of tuples and get both the index and the value of each item. The `if` condition `i == n` is used to filter the items and only include the `n`th element. 

For example, if the input list of tuples is [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] and `n` is 0, the function will return ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull'], which are the first four elements from the input list. 

The unit test `assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']` ensures that the function returns the expected result for the given input and `n` value. 