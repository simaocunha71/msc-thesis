```
def text_match_wordz(text):
    return 'z' in text
```
The function `text_match_wordz` checks if the string `text` contains the character 'z'. The unit test `assert text_match_wordz("pythonz.")==True` suggests that the function should return `True` if 'z' is found in the string and `False` otherwise. The function uses the `in` operator to check if 'z' is present in the string. If 'z' is found, the function returns `True`; otherwise, it returns `False`. This function is case-sensitive, meaning it treats 'z' and 'Z' as different characters. If you want a case-insensitive match, you can convert the text to lowercase or uppercase before checking for 'z'. For example: `return 'z' in text.lower()`. 