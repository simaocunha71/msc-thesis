```
def odd_values_string(s):
    return ''.join([s[i] for i in range(len(s)) if i % 2 == 0])
```
This function works by iterating over the indices of the string, and for each index, it checks if the index is even (i.e., `i % 2 == 0`). If the index is even, it includes the character at that index in the resulting string. The `join` function is used to concatenate the characters into a single string.

For example, for the string 'abcdef', the indices are 0, 1, 2, 3, 4, 5. The even indices are 0, 2, 4, so the function returns 'ace'.  ###########

Note: The unit test `assert odd_values_string('abcdef') == 'ace'` helps to clarify the problem and ensures that the function is working correctly. It checks that the function returns 'ace' when given the string 'abcdef'. This helps to ensure that the function is removing the characters at odd index values correctly.