```
def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')
```


The function `replace_specialchar` replaces all occurrences of spaces, commas, or dots with a colon. It uses the `replace` method of the string, which replaces all occurrences of the specified substring with another substring. The function is tested with the string 'Python language, Programming language.', and it returns 'Python:language::Programming:language:' as expected.