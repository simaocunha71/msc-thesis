```
def sample_nam(names):
    return sum(len(name) for name in names if name[0].isupper())
```


This function takes a list of names as input and returns the sum of the lengths of the names that start with an uppercase letter. It uses a generator expression to iterate over the names and filter out the ones that start with a lowercase letter using the `isupper()` method. The `sum()` function is then used to calculate the total length of the remaining names.

The unit test `assert sample_nam(['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith'])==16` ensures that the function works correctly by comparing the result with the expected output. In this case, the function should return `16` because the names 'Dylan', 'Diana', and 'Joanne' start with an uppercase letter and have lengths `5`, `5`, and `7` respectively, resulting in a total length of `16`. The names 'sally', 'rebecca', and 'keith' are filtered out because they start with a lowercase letter.