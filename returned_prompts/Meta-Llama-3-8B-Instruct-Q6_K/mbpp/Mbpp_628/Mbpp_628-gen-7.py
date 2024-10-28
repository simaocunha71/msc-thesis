```
def replace_spaces(s):
    return s.replace(' ', '%20')
```


Python's built-in string method `replace` can be used to replace all spaces in a string with '%20'. The `replace` method takes two arguments: the substring to replace and the replacement string. It returns a new string with all occurrences of the substring replaced with the replacement string. In this case, we use it to replace all spaces with '%20'. 

The unit test `assert replace_spaces("My Name is Dawood") == 'My%20Name%20is%20Dawood'` ensures that the function works correctly. It checks that the function replaces all spaces in the input string with '%20' and returns the resulting string. 

The time complexity of this solution is O(n), where n is the length of the input string, because the `replace` method needs to iterate over the entire string to find and replace all spaces. The space complexity is O(n) as well, because the function returns a new string that is potentially longer than the input string. 





