```
def replace_spaces(s):
    s = s.replace(' ', '_')
    s = s.replace('_', ' ')
    return s
```


Explanation:
The task is to create a function that replaces all whitespaces in a given string with an underscore and vice versa. This means that if the string contains a whitespace, it will be replaced with an underscore, and vice versa.

The provided unit test `assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'` helps to understand the task better. It shows that the function should replace all spaces in the string with underscores, effectively converting all spaces to underscores.

Here is the Python function that solves the problem:
```
def replace_spaces(s):
    s = s.replace(' ', '_')
    s = s.replace('_', ' ')
    return s
```
This function works by first replacing all spaces in the string with underscores using the `replace` method. Then, it replaces all underscores with spaces. This effectively achieves the desired result of replacing whitespaces with an underscore and vice versa. The function returns the modified string.