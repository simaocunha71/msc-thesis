```
def replace_specialchar(s):
    s = s.replace(' ', ':')
    s = s.replace(',', ':')
    s = s.replace('.', ':')
    return s
```


Explanation:
The problem is asking to create a function that replaces all occurrences of spaces, commas, or dots with a colon. The function takes a string as input and returns the modified string.

The unit test `assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')` helps to clarify the problem by showing the expected output for a given input.

The solution uses the `replace` method of the string class in Python, which replaces all occurrences of a specified substring with another substring. In this case, we replace spaces, commas, and dots with a colon. The modified string is then returned as the result of the function. 