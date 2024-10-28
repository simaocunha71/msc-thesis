```
def odd_values_string(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
```


Explanation: 
The problem is asking to create a function that takes a string as an input and returns a new string where all characters at odd indices are removed. For example, if the input string is 'abcdef', the output should be 'ace'.

The unit test provided, `assert odd_values_string('abcdef') == 'ace'`, helps to understand the problem better. It indicates that the function should return 'ace' when the input is 'abcdef'.

To solve this problem, we can use a list comprehension to iterate over the input string. We use the range function to generate indices for the string, and then use a conditional statement to check if the index is even. If the index is even, we include the character at that index in the new string. Finally, we use the join function to concatenate the characters in the new string into a single string.

Here's the Python function that implements this solution:
```
def odd_values_string(s):
    return ''.join(s[i] for i in range(len(s)) if i % 2 == 0)
```


This function works by iterating over the input string `s` using the range function, which generates indices from 0 to the length of the string minus 1. It then uses a conditional statement to check if the index `i` is even (i.e., `i % 2 == 0`). If the index is even, it includes the character at that index in the new string. Finally, it uses the join function to concatenate the characters in the new string into a single string, which is returned as the result.