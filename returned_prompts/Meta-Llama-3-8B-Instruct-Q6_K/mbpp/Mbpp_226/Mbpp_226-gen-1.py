```
def odd_values_string(s):
    return ''.join([char for i, char in enumerate(s) if i % 2 == 0])
```
This function uses list comprehension and the enumerate function to iterate over the string. The enumerate function returns both the index and the value of each character in the string. The list comprehension then selects only the characters at even index values (i.e., where i % 2 == 0) and joins them together into a new string. 

For example, if the input string is 'abcdef', the function will return 'ace', which are the characters at even index values (0, 2, and 4) of the original string. 

The unit test `assert odd_values_string('abcdef') == 'ace'` ensures that the function works correctly for this specific input. 