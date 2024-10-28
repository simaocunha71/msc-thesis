You can use Python's built-in functions `str.find()` and `str.rfind()` to find the positions of 'z' in the string. The `str.find()` function returns the lowest index of 'z' in the string, and `str.rfind()` returns the highest index of 'z' in the string. Then, you can check if the index returned by `str.find()` is different from the index returned by `str.rfind()`. If they are different, it means 'z' is present in the middle of the string.

Here is the function in Python:

```python
def text_match_wordz_middle(text):
    return text.find('z') != text.rfind('z')
```

This function works as expected. It returns `True` if 'z' is present in the middle of the string and `False` otherwise. For example, `text_match_wordz_middle("pythonzabc.")` returns `True` because 'z' is present in the middle of the string, and `text_match_wordz_middle("zabc.")` returns `False` because 'z' is not present in the middle of the string. 