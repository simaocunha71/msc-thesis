```
def odd_values_string(s):
    return ''.join([c for i, c in enumerate(s) if i % 2 == 0])
```
The function `odd_values_string` takes a string `s` as input and returns a new string where all characters at odd index positions are removed. The `enumerate` function is used to get both the index and value of each character in the string. The `if i % 2 == 0` condition checks if the index is even, and if so, the character is included in the new string. The `join` function is used to concatenate the characters into a new string. 

For example, if the input string is 'abcdef', the function will return 'ace' because the characters at odd index positions ('b' and 'd') are removed. 

The unit test `assert odd_values_string('abcdef') == 'ace'` ensures that the function behaves as expected.  It checks that the output of the function with input 'abcdef' is indeed 'ace'. 

This solution has a time complexity of O(n), where n is the length of the input string, because it iterates over each character in the string once. The space complexity is O(n) as well, because it creates a new string of potentially different length.  The function is case-sensitive and does not handle non-string inputs.  It also assumes that the input string is not empty.  If these assumptions are not valid, additional error handling would be necessary. 