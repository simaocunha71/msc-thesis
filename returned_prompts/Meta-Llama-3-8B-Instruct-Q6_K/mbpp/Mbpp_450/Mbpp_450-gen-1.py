You can solve this problem by defining a function that takes a list of strings and an integer as arguments. The function will then use a list comprehension to iterate over the list of strings, filter out the strings with lengths less than the specified integer, and return the filtered list.

Here is the solution in Python:
```
def extract_string(lst, size):
    return [s for s in lst if len(s) >= size]
```
This function uses a list comprehension to create a new list that contains only the strings from the original list that have lengths greater than or equal to the specified size. The `len(s) >= size` condition is used to filter out the strings that are shorter than the specified size.

The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` ensures that the function works correctly. It checks that the function returns the expected list of strings when given the specified list and size as input. If the function works correctly, the test will pass; otherwise, it will raise an AssertionError.