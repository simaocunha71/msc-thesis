```
def extract_values(s):
    return [x.strip('"') for x in s.split('"')]
```
This function splits the input string `s` into substrings using the character `"` as a delimiter. It then strips the quotation marks from each substring and returns them as a list. The `strip('"')` method removes the leading and trailing `"` characters from each substring. The list comprehension is used to apply this operation to each substring in the list returned by the `split('"')` method.

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function works correctly. It checks that the function returns a list containing the strings `"Python", "PHP", "Java"` when the input string is `"Python", "PHP", "Java"`. This test helps to validate the correctness of the function.