You can use the re module in Python to extract values between quotation marks from a string. The function will split the string by the quotation marks and return a list of extracted values.

Here is the function:

```
import re

def extract_values(s):
    return re.findall(r'"([^"]*)"', s)
```

This function uses the findall function from the re module to find all occurrences of the pattern '"([^"]*)"' in the string. The pattern '"([^"]*)"' matches a quotation mark followed by any characters that are not a quotation mark, and then a quotation mark. The parentheses around the "([^"]*)'" part create a capture group, which is used to extract the matched text. The findall function returns a list of all matches. 

For example, if you call `extract_values('"Python", "PHP", "Java"')`, it will return `['Python', 'PHP', 'Java']`. 

This function assumes that the quotation marks are double quotation marks. If you want to extract values between single quotation marks, you can modify the pattern to '"([^']*)"' or if you want to extract values between both single and double quotation marks, you can use a more complex pattern. 

The unit test `assert extract_values('"Python", "PHP", "Java"')==['Python', 'PHP', 'Java']` ensures that the function works correctly. It checks if the function returns the expected output for a given input. If the function returns the expected output, the test passes; otherwise, it fails. 

You can add more unit tests to ensure that the function works correctly for different inputs. For example, you could add tests for inputs with single quotation marks, or inputs with both single and double quotation marks. 

You can also add error handling to the function. For example, you could check if the input string is None or empty before trying to extract values from it. This would prevent the function from throwing an error if the input is invalid. 

Here is the function with error handling:

```
import re

def extract_values(s):
    if s is None or s == '':
        return []
    return re.findall(r'"([^"]*)"', s)
``` 

This version of the function returns an empty list if the input string is None or empty, instead of throwing an error. This makes the function more robust and easier to use. 