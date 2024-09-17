```
def remove_all_spaces(s):
    return s.replace(" ","")
```
This function uses the replace() method of the string to replace all spaces with an empty string, effectively removing all spaces. The unit test `assert remove_all_spaces('python  program')==('pythonprogram')` ensures that the function works as expected. 

For example, if you call `remove_all_spaces('python  program')`, it will return `'pythonprogram'`. 

This function will work for any string, not just the one specified in the unit test. 

The time complexity is O(n), where n is the length of the string, because the replace() method needs to iterate over the entire string to find all spaces. The space complexity is O(n), because the replace() method returns a new string that is a copy of the original string with all spaces removed. 

The function is case-sensitive, meaning it will treat uppercase and lowercase spaces differently. If you want a case-insensitive solution, you can use the `replace()` method in a loop, or use regular expressions. 

Here's an example of a case-insensitive solution using regular expressions:
```
import re
def remove_all_spaces(s):
    return re.sub(r'\s+', '', s)
```
This function uses the `re.sub()` function to replace all whitespace characters (`\s+`) with an empty string. The `r` before the pattern string indicates a raw string, which is useful when working with regular expressions. The `+` after `\s` means "one or more" whitespace characters, so this function will remove all whitespace characters, not just single spaces. 

This function is also O(n) in time complexity and O(n) in space complexity, and it is case-insensitive. 