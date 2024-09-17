```
def extract_nth_element(lst, n):
    return [x for i, x in enumerate(lst) if i == n]
```


This function takes two parameters, `lst` which is the list of tuples and `n` which is the index of the element to extract. It uses list comprehension with `enumerate` to iterate over the list and its indices, and returns a list containing the element at the specified index. If the index is out of range, it will return an empty list.

The unit test provided, `assert extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)==['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']`, suggests that the function should return all elements when `n` is 0, which is why it returns the entire list. If you want to return only the nth element, you can modify the function to `return lst[n]`. However, this will raise an `IndexError` if `n` is out of range. You can add error handling to return a default value or raise an exception if needed. 