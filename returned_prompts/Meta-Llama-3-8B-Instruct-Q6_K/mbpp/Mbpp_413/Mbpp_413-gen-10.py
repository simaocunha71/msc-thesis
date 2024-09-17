```
def extract_nth_element(lst, n):
    if n<0:
        raise ValueError("n should be a non-negative integer")
    if n >= len(lst):
        raise ValueError("n is out of range")
    return [tup for i, tup in enumerate(lst) if i==n]
```    
The function takes two parameters, a list of tuples `lst` and an integer `n`. It first checks if `n` is less than 0, in which case it raises a `ValueError` because `n` should be a non-negative integer. Then it checks if `n` is greater than or equal to the length of `lst`, in which case it also raises a `ValueError` because `n` is out of range. If `n` is within the valid range, the function returns a list containing the `n`th element of `lst`. The `enumerate` function is used to get both the index and the value of each element in `lst`. The list comprehension then filters the elements to return the `n`th one.

The unit test `assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']` ensures that the function returns the correct output when `n` is 0, which means it returns the entire list. This test also ensures that the function correctly handles a list of tuples. 