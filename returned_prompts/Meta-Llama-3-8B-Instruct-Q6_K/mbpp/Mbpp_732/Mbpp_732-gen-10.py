```
def replace_specialchar(s):
    return s.replace(" ", ":").replace(",", ":").replace(".", ":")
```





Python's built-in string method `replace()` is used to replace all occurrences of spaces, commas, or dots with a colon. The `replace()` method returns a copy of the string where all occurrences of a substring have been replaced with another substring. It takes two parameters: the substring to be replaced, and the substring that will replace it. In this case, we use it three times, replacing spaces with a colon, commas with a colon, and dots with a colon. The result is returned as a string. 

The unit test `assert replace_specialchar('Python language, Programming language.')==('Python:language::Programming:language:')` ensures that the function works correctly. It checks if the output of the function `replace_specialchar('Python language, Programming language.')` is equal to `'Python:language::Programming:language:'`. If they are equal, the test passes. If they are not equal, the test fails. 

This function assumes that the input is a string. If the input is not a string, the function may not work as expected. It is also case-sensitive, so it will treat uppercase and lowercase letters differently. If you want a case-insensitive replacement, you can convert the string to lowercase or uppercase before replacing the characters. 





This is a simple function that can be used to replace specific characters in a string with a specified replacement character. It can be used in a variety of situations, such as preprocessing text data or formatting strings for a specific purpose. The function is easy to understand and use, and it works correctly as long as the input is a string. If you need to replace a large number of characters, you can add more `replace()` calls to the function. If you need to replace characters in a specific order, you may need to use a different approach, such as using regular expressions or iterating over the characters in the string.