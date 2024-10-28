```
def extract_nth_element(lst, n):
    return [t for i, t in enumerate(lst) if i == n]
```
This function uses list comprehension to extract the nth element from the given list of tuples. The `enumerate` function is used to get both the index and the value of each tuple in the list. The `if i == n` condition is used to filter the list and only include the tuple at the nth index. 

For example, if you call `extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)`, the function will return `['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']`, which are all the tuples in the list. 

If you call `extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,1)`, the function will return `['Brady Kent', 'Wyatt Knott', 'Beau Turnbull']`, which are all the tuples except the first one. 

And so on. The function will return all the tuples up to and including the nth one, and none of the tuples after that. 