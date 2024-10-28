```
def extract_string(lst, size):
    return [s for s in lst if len(s) == size]
```
This function uses list comprehension to iterate over the input list and filter out the strings that have the specified size. The filtered list of strings is then returned.

For example, if you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] , 8)`, it will return `['practice', 'solution']` because these are the strings in the input list that have a length of 8. 

The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` ensures that the function works correctly.  If the function works correctly, it will return `['practice', 'solution']`, which is the expected output for the given input.  If the function does not work correctly, it will raise an AssertionError.  This helps to catch any errors in the function and ensures that it works correctly. 