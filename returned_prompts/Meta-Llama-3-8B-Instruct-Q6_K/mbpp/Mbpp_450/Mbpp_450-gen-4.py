```
def extract_string(lst, size):
    return [string for string in lst if len(string) == size]
```
This function takes a list of strings and an integer size as input. It then uses a list comprehension to create a new list that contains only the strings from the original list that have the specified size. The function returns this new list.

The unit test provided ensures that the function works correctly. The test case `assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']` checks that the function returns the strings 'practice' and 'solution' when given the list `['Python', 'list', 'exercises', 'practice', 'solution']` and the size 8. This is because 'practice' and 'solution' are the only strings in the list with a length of 8. The function passes this test, indicating that it is working correctly. 