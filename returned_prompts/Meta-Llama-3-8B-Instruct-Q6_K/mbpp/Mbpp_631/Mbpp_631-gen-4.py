```
def replace_spaces(s):
    return s.replace(' ', '_').replace('_', ' ')
```
This function uses the `replace` method to replace all spaces with underscores and then all underscores with spaces. The result is a string where all spaces have been replaced with underscores, and vice versa. The unit test `assert replace_spaces('Jumanji The Jungle') == 'Jumanji_The_Jungle'` helps to clarify the problem by showing that all spaces should be replaced with underscores, and vice versa.