```
def text_match_wordz_middle(text):
    return 'z' in text[1:-1]
```
The function `text_match_wordz_middle` takes a string `text` as an argument. It checks if the character 'z' is present in the string, excluding the first and last characters. This is achieved by using Python's string slicing feature. The expression `text[1:-1]` returns a slice of the string from the second character to the second last character. The `in` operator is used to check if 'z' is present in this slice. If 'z' is found, the function returns `True`; otherwise, it returns `False`. The unit test `assert text_match_wordz_middle("pythonzabc.")==True` passes, indicating that the function is working correctly.