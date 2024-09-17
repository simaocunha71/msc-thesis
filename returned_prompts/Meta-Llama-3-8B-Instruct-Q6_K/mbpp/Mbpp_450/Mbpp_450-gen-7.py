```
def extract_string(lst, size):
    return [string for string in lst if len(string) == size]
```


This function uses a list comprehension to iterate over the input list and includes only the strings that have the specified length. In this case, it filters the list to include only the strings with a length of 8. The resulting list is then returned. 

The unit test provided ensures that the function works correctly, as it checks that the function returns the expected output when given a specific input. 

The unit test is:
```
assert extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)==['practice', 'solution']
```


This test checks that the function returns the list `['practice', 'solution']` when given the list `['Python', 'list', 'exercises', 'practice', 'solution']` and the size `8`. If the function is working correctly, this test will pass. If the function is not working correctly, this test will fail, indicating that there is an error in the function. 





This function takes two parameters: a list of strings (`lst`) and an integer (`size`). It returns a new list that includes only the strings from the input list that have the specified length. The function uses a list comprehension to iterate over the input list and includes only the strings that have the specified length. The resulting list is then returned.

For example, if you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,8)`, the function will return `['practice', 'solution']` because these are the only strings in the input list that have a length of 8. If you call `extract_string(['Python', 'list', 'exercises', 'practice', 'solution'] ,5)`, the function will return `['list', 'exercises']` because these are the only strings in the input list that have a length of 5.