```
def extract_string(lst, size):
    return [s for s in lst if len(s) == size]
```
The function `extract_string` takes a list of strings `lst` and an integer `size` as input. It uses a list comprehension to iterate over the input list and returns a new list containing only the strings that have the specified length (`size`). The `len(s) == size` condition in the list comprehension ensures that only the strings of the specified length are included in the output list. If no strings of the specified length are found, the function returns an empty list.

The unit test `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` ensures that the function works correctly by checking if the function returns the expected output for the given input. In this case, the function should return `['practice', 'solution']` because these are the strings in the input list that have a length of 8. If the function returns anything else, the unit test will fail.