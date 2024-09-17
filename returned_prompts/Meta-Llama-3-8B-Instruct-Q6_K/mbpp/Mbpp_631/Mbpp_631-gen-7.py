```
def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')
``` 

The problem asks to write a function that takes a string as input and replaces all whitespaces with underscores and vice versa. 

The unit test `assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'` suggests that we should replace all spaces with underscores and then replace all underscores with spaces. 

Here is a Python function that accomplishes this:

```python
def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')
```

This function uses the `replace` method of the string, which replaces all occurrences of a substring with another substring. In this case, we first replace all spaces with underscores, and then replace all underscores with spaces. The result is a string where all whitespaces have been replaced with underscores and vice versa. 