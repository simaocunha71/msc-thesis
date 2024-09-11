def extract_nth_element(lst, n):
    extracted = []
    for i in range(len(lst)):
        if i == n:
            extracted.append(lst[i][0])
    return extracted


# Test
print(extract_nth_element([('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] ,0)) # Expected: ['Greyson Fulton', 'Brady Kent', 'Wyatt Knott', 'Beau Turnbull']


"""
The function works by iterating over the given list of tuples, and for each tuple, it checks if the current index matches the desired index. If it does, it adds the first element of the tuple to the extracted list. Finally, it returns the extracted list.

In the provided test case, the desired index is 0, so the function extracts the first element of the first tuple and returns the result.
"""

```python
def extract_nth_element(lst, n):
    extracted = []
    for i in range(len(lst)):
        if i == n:
            extracted.append(lst[i][0])
    return extracted
```

This function will extract the nth element from a given list of tuples and return it as a new list. It works by iterating over the input list and checking if the current index matches the desired index. If it does, it appends the first element of the tuple to the extracted list. Finally, it returns the extracted list.

For example, if we pass `[('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)]` as the input list and `0` as the desired index, the function will extract the first element of the first tuple (`'Greyson Fulton'`) and return it as a new list `['Greyson Fulton']`.