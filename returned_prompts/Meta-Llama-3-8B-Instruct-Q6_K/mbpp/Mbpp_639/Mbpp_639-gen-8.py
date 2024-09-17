```
def sample_name(names):
    return sum(len(name) for name in names if name[0].isupper())
```


This function takes a list of names as input and returns the sum of the lengths of the names that start with an uppercase letter. It uses a generator expression to iterate over the names, and the built-in `isupper()` method to check if the first letter of each name is uppercase. If the name starts with an uppercase letter, its length is added to the sum. The `sum()` function then returns the total length of these names. The unit test `assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16` shows that the function works correctly. 