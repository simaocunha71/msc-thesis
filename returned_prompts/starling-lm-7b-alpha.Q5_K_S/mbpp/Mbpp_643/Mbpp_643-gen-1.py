```python
def text_match_wordz_middle(text):
    return 'z' in text and text[0] != 'z' and text[-1] != 'z'
```

In this program, the function `text_match_wordz_middle` is defined to take a string `text` as an input. It uses the `in` operator to check if the string contains the character 'z'. Additionally, it checks if the first character of the string is not 'z' and if the last character of the string is not 'z' using the indexing feature of strings in Python. If all these conditions are satisfied, the function returns `True`, indicating that the string contains 'z' only in the middle of the word.

To test the function, the assertion `text_match_wordz_middle("pythonzabc.")==True` is used. This means that the function should return `True` for the input string "pythonzabc.". The function correctly identifies that 'z' is present in the string and not at the start or end, so it returns `True`.

Overall, the function `text_match_wordz_middle` is a simple and efficient solution to check if a string contains 'z' in the middle of the word, while excluding the cases where 'z' is at the start or end of the string.

```python
def text_match_wordz_middle(text):
    return 'z' in text and text[0] != 'z' and text[-1] != 'z'
```

This code defines a function called `text_match_wordz_middle` that takes a string `text` as an argument. The function uses the `in` operator to check if 'z' is present in the string `text`. Additionally, it checks if the first character of the string is not 'z' and if the last character of the string is not 'z' using indexing. If all these conditions are satisfied, the function returns `True`, indicating that the string contains 'z' only in the middle of the word.

To test the function, the assertion `text_match_wordz_middle("pythonzabc.")==True` is used. This means that the function should return `True` for the input string "pythonzabc.". The function correctly ident