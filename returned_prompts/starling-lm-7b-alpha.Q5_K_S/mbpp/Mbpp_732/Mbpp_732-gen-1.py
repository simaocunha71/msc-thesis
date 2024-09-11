```
def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')
```

# Python language, Programming language.
replace_specialchar('Python language, Programming language.')

# Output: Python:language::Programming:language:

This function replaces all occurrences of the specified characters with a colon.

Explanation:
The function `replace_specialchar` takes a string `s` as input. It uses the `replace()` method to replace all occurrences of the space character with a colon, then all occurrences of the comma character with a colon, and finally all occurrences of the dot character with a colon. The modified string is then returned as the output.

In the provided example, the function `replace_specialchar` is called with the string `'Python language, Programming language.'`. The function replaces all spaces, commas, and dots with colons, resulting in the output `'Python:language::Programming:language:'`.

The `assert` statement is used to verify that the function produces the expected output.

Overall, this solution effectively replaces the specified characters in a string with colons, as required by the problem statement.














































```
```