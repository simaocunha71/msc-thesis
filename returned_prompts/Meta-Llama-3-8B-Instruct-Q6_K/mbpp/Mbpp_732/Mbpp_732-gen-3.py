```
def replace_specialchar(s):
    return s.replace(' ', ':').replace(',', ':').replace('.', ':')
```


In this function, the replace() method is used to replace all occurrences of spaces, commas, and dots with a colon. The replace() method returns a copy of the string where all occurrences of a substring are replaced with another substring. The replace() method does not modify the original string but returns a new string. The function takes a string s as an argument and returns a new string where all spaces, commas, and dots have been replaced with a colon. The unit test `assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')` checks the function's output. 

For example, if you call `replace_specialchar('Python language, Programming language.')`, it will return `'Python:language::Programming:language:'`. The function works correctly because it replaces all spaces, commas, and dots with a colon. 

The unit test `assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')` ensures that the function works correctly for the given test case. If the function does not work correctly, the unit test will fail, indicating that there is a bug in the function. 

The function is simple and easy to understand, making it a good choice for a problem that requires replacing special characters in a string. The replace() method is a built-in Python method that is easy to use and works well for this type of problem. 

The function can be further improved by adding more error checking to handle edge cases, such as an empty string or a string with no special characters. However, for the given problem, the function works correctly and is easy to understand. 

The function is efficient because it uses the replace() method, which is a built-in Python method that is optimized for performance. The function does not create any unnecessary data structures or perform any unnecessary computations, making it efficient for large inputs. 

The function is also flexible because it can be easily modified to replace other special characters by adding more replace() calls. For example, you could add a replace() call to replace semicolons with colons. The function is easy to extend and modify, making it a good choice for a problem that requires replacing multiple special characters. 