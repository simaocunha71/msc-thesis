Here is the Python function:

```python
def sum_names(names):
    return sum(len(name) for name in names if not name[0].islower())

print(sum_names(['sally', 'Dylan',  'rebecca', 'Diana', 'Joanne', 'keith']))  # Output: 16
```

This function works by using a generator expression inside the `sum` function. It loops over each name in the `names` list and includes its length in the sum if the first character of the name is not a lowercase letter. The `islower` method of the string class checks if all the characters are in lowercase. If all are not, it returns `False`. Otherwise, it returns `True`. Therefore, we use the `not` operator to get `True` for names that start with a lowercase letter, and `False` for names that start with an uppercase letter.

This function works as required for the sample input.

Note: This function assumes that all the names in the list are strings. If the list contains non-string elements, this function