```
def sample_nam(lst):
    return sum(len(name) for name in lst if name[0].isupper())
```
The function `sample_nam` takes a list of names as input. It uses a generator expression to iterate over each name in the list. For each name, it checks if the first character is an uppercase letter using the `isupper()` method. If the name starts with an uppercase letter, it calculates the length of the name using the `len()` function and adds it to the total sum. The function then returns the total sum of the lengths of the names that start with an uppercase letter. 

The unit test `assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16` ensures that the function works correctly. It checks if the sum of the lengths of the names 'Dylan', 'Diana', and 'Joanne' is 16, which it is. 

This function assumes that the input list contains only strings. If the list can contain non-string values, you should add error handling code to handle this case. 