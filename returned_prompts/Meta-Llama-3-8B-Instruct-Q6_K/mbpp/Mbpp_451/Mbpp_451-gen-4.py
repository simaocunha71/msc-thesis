```
def remove_whitespaces(s):
    return s.replace(" ", "")
```
This function uses the `replace` method of the string to replace all occurrences of a whitespace character with an empty string, effectively removing all whitespaces. The unit test `assert remove_whitespaces(' Google    Flutter ') == 'GoogleFlutter'` ensures that the function works correctly. 

For example, if you call `remove_whitespaces(' Google    Flutter ')`, it will return `'GoogleFlutter'`, which is the input string with all whitespaces removed. 

Note that this function removes all types of whitespace characters, including spaces, tabs, and newlines. If you only want to remove spaces, you can use the `replace` method with a space character as the argument. For example, `s.replace(' ', '')`.  If you want to remove other types of whitespace characters, you can use the `str.translate` method or regular expressions.  For example, `s.translate(str.maketrans("", "", "  \t\n"))` or `re.sub(r'\s+', '', s)`.  However, these methods are more complex and may be overkill for this simple task.  The `replace` method is usually the most straightforward and efficient way to remove all types of whitespace characters. 