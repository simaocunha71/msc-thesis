```
def odd_values_string(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
```
This function works by iterating over the string using a for loop and checking if the index of the character is even. If the index is even, it includes the character in the new string. The result is a new string with characters at even index values. The unit test `assert odd_values_string('abcdef') == 'ace'` helps to clarify this problem by providing an example of the expected output. 
Note: The problem statement seems to be asking for characters at even index values, but the unit test provided suggests that it's asking for characters at odd index values. I've written the solution assuming the unit test is correct. If the problem statement is correct, the solution would be `def odd_values_string(s): return ''.join(s[i] for i in range(1, len(s), 2))`. 
The unit test `assert odd_values_string('abcdef') == 'ace'` is checking if the function returns the string 'ace' when given the input 'abcdef'. This suggests that the function should return a string with characters at odd index values. 
However, if the problem statement is asking for characters at even index values, the function should return the string 'ace'. In this case, the unit test is incorrect and the problem statement should be revised. 





```python
def odd_values_string(s):
    return ''.join(s[i] for i in range(1, len(s), 2))
```
This solution works by using a generator expression to iterate over the string `s`. The `range` function is used to generate indices from 1 to the length of the string, with a step size of 2. This means that the indices will be 1, 3, 5, ... which are the odd index values. The `join` method is then used to concatenate the characters at these indices into a new string.